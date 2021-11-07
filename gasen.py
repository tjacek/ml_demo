import random

class MockEnsemble(object):
    def __init__(self,n_clfs=3,n_cats=5):
        self.clfs=[ MockClf(i,n_cats) 
            for i in range(n_clfs)]	
        self.n_cats=n_cats

    def __call__(self,n_iters=100):
        y_true=[(i % self.n_cats) for i in range(n_iters)]
        y_pred=[[clf_j(i) for clf_j in self.clfs] 
    	            for i in y_true]
        return y_true,list(zip(*y_pred))

class MockClf(object):
    def __init__(self,wrong,n_cats=5):
        self.wrong=wrong
        self.n_cats=n_cats
        
    def __call__(self,i):
        if(self.wrong==i):
        	threshold=0.1
        else:
            threshold=0.9	
        if(random.uniform(0,1)<threshold):
            return i
        return random.randrange(self.n_cats)

ens=MockEnsemble()
print(ens(30)[1][0])