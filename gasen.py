import numpy as np
import random
from scipy.optimize import differential_evolution
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

class MockEnsemble(object):
    def __init__(self,n_clfs=3,n_cats=3):
        self.clfs=[ WrongCat(0,n_cats),WrongCat(0,n_cats),
                    RightCat(0)]	
        self.n_cats=n_cats

    def __call__(self,n_iters=100):
        y_true=[(i % self.n_cats) for i in range(n_iters)]
        y_pred=[[clf_j(i) for clf_j in self.clfs] 
    	            for i in y_true]
        return y_true,list(zip(*y_pred))

class WrongCat(object):
    def __init__(self,wrong,n_cats=5,threshold=0.5):
        self.wrong=wrong
        self.n_cats=n_cats
        self.threshold=threshold

    def __call__(self,i):
        if(random.uniform(0,1)<self.threshold):
            return self.wrong
        return i

class RightCat(object):
    def __init__(self,right,n_cats=3,threshold=0.3):
        self.right=right
        self.n_cats=n_cats
        self.threshold=threshold

    def __call__(self,i):
        if(self.right==i):
            return i	
        if(random.uniform(0,1)<self.threshold):
            return random.randrange(self.n_cats)
        return i

def corl_error(y_true,preds):
    c=[[ np.dot(error(pred_i,y_true),error(pred_j,y_true))
            for pred_i in preds]
                for pred_j in preds]
    c=np.array(c)
    norm=(1/float(len(y_true)))
    return norm*c

def error( y_pred,y_true):
	return np.array([ int(pred_i!=true_i) 
	        for pred_i,true_i in zip(y_pred,y_true)])

def find_weights(C,max_iter=1000):
    size=C.shape[0]    
    bound_w = [(0.0, 1.0)  for _ in range(size)]
    def loss_fun(weights):
        norm=weights/np.sum(weights)
        E=np.dot(norm.T,np.dot(C,norm))
        return E
    result = differential_evolution(loss_fun, bound_w, maxiter=max_iter, tol=1e-7)
    weights=result['x']
    print(loss_fun(weights)/np.sum(weights))
    return weights

def exp(ens,n_samples=1000):
    y_true,preds= ens(n_samples)
    C=corl_error(y_true,preds)
    print(C)
    weights=find_weights(C)
    print(weights)
    voting(y_true,preds)
    voting(y_true,preds,weights)

def voting(y_true,preds,weights=None,n_cats=3):
    if(weights is None):
        preds=np.array([to_one_hot(pred_i,n_cats)
             for pred_i in preds])
    else:
        preds=np.array([weights[i]*to_one_hot(pred_i,n_cats)
             for i,pred_i in enumerate(preds)])	
    result= np.sum(preds,axis=0)
    final_pred=np.argmax(result,axis=0)
    acc=accuracy_score(y_true,final_pred)
    print(acc) 

def to_one_hot(y,n_cats):
    hot=np.zeros((n_cats,len(y)))
    for i,y_i in enumerate(y):
        hot[y_i,i]=1
    return hot

def plot_loss(ens,n_samples=1000): 
    y_true,preds= ens(n_samples)
    C=corl_error(y_true,preds)
    def loss(weights):
        weights=np.array(weights)
        return np.dot(weights.T,np.dot(C,weights))
    x = np.arange(-1.0, 1.0, 0.1)
    y = np.arange(-1.0, 1.0, 0.1)
    z=[[ loss([x_i,y_i,0])  
         for x_i in x]
            for y_i in y]
    z=np.array(z)
    fig, ax = plt.subplots()
    CS = ax.contour(x, y, z)
    ax.clabel(CS, inline=False, fontsize=10)
    ax.set_title('Simplest default with labels')
    plt.show()

ens=MockEnsemble()
plot_loss(ens,n_samples=1000)