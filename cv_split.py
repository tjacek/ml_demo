import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
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
        return X,y

    def split(self,select=None):
        if( select is None):
            select=lambda name_i: (name_i.get_cat()%2)==0 
        train,test=DataDict(),DataDict()
        for name_i in self.keys():
            if(select(name_i)):
                train[name_i]=self[name_i]
            else:
                test[name_i]=self[name_i]
        return train,test

class Ensemble(object):
    def __init__(self,clfs):
        self.clfs=clfs

    def train(self,dataset:DataDict):
        X,y=dataset.as_xy()
        return [clf_i.fit(X,y) for clf_i in self.clfs]

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
    clfs = [DecisionTreeClassifier(max_depth=4),
            KNeighborsClassifier(n_neighbors=7),
            SVC(gamma=0.1, kernel="rbf", probability=True)]
    return Ensemble(clfs)

X, y = load_iris(return_X_y=True)
dataset=to_data_dict(X,y)
ens=get_simple_ensemble()
ens.train(dataset)