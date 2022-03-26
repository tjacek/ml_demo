import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier

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
        name_i=Name(f"{y_i-1}_{cats_size[y_i]}")
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

X, y = load_iris(return_X_y=True)
dataset=to_data_dict(X,y)
ensemble=get_simple_ensemble()
cv_split(dataset,ensemble)
