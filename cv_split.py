from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier

class Ensemble(object):
    def __init__(self,clfs):
        self.clfs=clfs

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


def get_simple_ensemble():
    clfs = [DecisionTreeClassifier(max_depth=4),
            KNeighborsClassifier(n_neighbors=7),
            SVC(gamma=0.1, kernel="rbf", probability=True)]
    return Ensemble(clfs)

X, y = load_iris(return_X_y=True)
print(y)