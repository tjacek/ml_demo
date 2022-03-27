import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import classification_report
from scipy.optimize import differential_evolution
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import LabelBinarizer

class Name(str):
    def __new__(cls, p_string):
        return str.__new__(cls, p_string)

    def get_cat(self):
        return int(self.split('_')[0])-1

    def get_person(self):
        return int(self.split('_')[1])

class DataDict(dict):
    def __init__(self, arg=[]):
        super(DataDict, self).__init__(arg)

    def __setitem__(self, key, value):
        if(type(key)!=Name):
            key=Name(key)
        super(DataDict, self).__setitem__(key, value)

    def as_xy(self):
        names=self.keys()
        X=np.array([self[name_i] for name_i in names])
        y=[name_i.get_cat()+1 for name_i in names]
        return X,y,names

    def split(self,select=None):
        if( select is None):
            select=lambda name_i: (name_i.get_person()%2)==0 
        train,test=DataDict(),DataDict()
        for name_i in self.keys():
            if(select(name_i)):
                train[name_i]=self[name_i]
            else:
                test[name_i]=self[name_i]
        return train,test

class Ensemble(object):
    def __init__(self,algs):
        self.algs=algs

    def __len__(self):
        return len(self.algs)

    def train_clf(self,train):
        X_train,y_train,names=train.as_xy()
        return [alg_i.fit(X_train,y_train) 
                    for alg_i in self.algs]

    def get_votes(self,train,test):
        clfs=self.train_clf(train)
        X_test,y_test,names=test.as_xy()
        votes_dict={ name_i:[] for name_i in names} 
        for clf_i in clfs:
            pred_i=clf_i.predict_proba(X_test)
            for j,name_j in enumerate( names):
                vote_ij=np.flip(np.argsort(pred_i[j]))
                votes_dict[name_j].append(vote_ij)
        return votes_dict

def to_data_dict(X,y):
    dataset=DataDict()
    cats_size={}
    for x_i,y_i in zip(X,y):
        if(not y_i in cats_size):
        	cats_size[y_i]=0
        cats_size[y_i]+=1
        name_i=Name(f"{y_i+1}_{cats_size[y_i]}")
        dataset[name_i]=x_i
    return dataset

def get_simple_ensemble():
    clfs = [LogisticRegression(),
            KNeighborsClassifier(n_neighbors=7),
            SVC(gamma=0.1, kernel="rbf", probability=True)]
    return Ensemble(clfs)

def cv_split(dataset,ensemble,n_split=5):
    train,test=dataset.split()
    all_votes={}
    for i in range(n_split):
        def select_i(name_i): 
            return (name_i.get_person()/2) % n_split ==i
        valid_train_i,valid_test_i =train.split(select_i)
        votes_i=ensemble.get_votes(valid_train_i,valid_test_i)
        all_votes={**all_votes ,**votes_i}
    return all_votes

def majority_voting(votes):
    y_true,y_pred=[],[]
    for name_i,votes_i in votes.items():
        y_true.append(name_i.get_cat())
        votes_i=np.array(votes_i)[:,0].T
        y_pred.append(np.bincount(votes_i).argmax()) 
    return y_true,y_pred

def posistional_voting(votes,weights):
    y_true,y_pred=[],[]
    n_cats=len(weights)
    for name_i,votes_i in votes.items():
        y_true.append(name_i.get_cat())
        counter= np.zeros((n_cats,))
        for votes_ij in votes_i:
            for t,cat_t in enumerate(votes_ij):
                counter[cat_t]+=weights[t]
        y_pred.append( np.argmax(counter))
    return y_true,y_pred

def init_borda(size,n_cats):
    popula=np.ones((size,n_cats))
    for i in range(n_cats):
        popula[:,i]=n_cats-i
    return popula

def base_exp(dataset):
    train,test=dataset.split()
    ensemble=get_simple_ensemble()
    votes=ensemble.get_votes(train,test)
    y_true,y_pred= majority_voting(votes)
    print( classification_report(y_true,y_pred))

def opv_exp(dataset):
    ensemble=get_simple_ensemble()
    cv_votes=cv_split(dataset,ensemble,n_split=5)
    def loss_fun(weights):
        weights/=np.sum(weights)
        y_true,y_pred=posistional_voting(cv_votes,weights)
        y_true= LabelBinarizer().fit_transform(y_true)
        y_pred= LabelBinarizer().fit_transform(y_pred)        
        auc_ovo=roc_auc_score(y_true,y_pred,multi_class="ovo")
        return -1.0*auc_ovo
    bound_w = [(0.0, 1.0)  for _ in range(len(ensemble))]
    weights= differential_evolution(loss_fun, bound_w, 
                init=init_borda(30,len(ensemble)),
                maxiter=1000, tol=1e-4)['x']
    train,test=dataset.split()
    votes=ensemble.get_votes(train,test)
    y_true,y_pred= posistional_voting(votes,weights)
    print(weights)    
    print( classification_report(y_true,y_pred))

X, y = load_iris(return_X_y=True)
dataset=to_data_dict(X,y)
base_exp(dataset)
opv_exp(dataset)