import numpy as np
import matplotlib.pyplot as plt

def make_plot(fun=None,n_frames=30,
	  title='Proposed distribution'):
    x=np.arange(n_frames)
    if(fun is None):
        y=x
    else:
    	y=fun(x)
    plt.bar(x, y) #color ='maroon',width = 0.4)
    plt.xlabel("Frames")
    plt.ylabel("Probability")
    plt.title(title)
    plt.show()

def proposed(x):
    start,end= 0,len(x)
    y=[min(d(start,i),d(i,end))**2 for i in x]
    return y/np.sum(y)

def d(i,j):
    return np.abs(i-j)	

class Normal(object):
    def __init__(self,sigma=3):
        self.sigma=sigma

    def __call__(self,x):
        mean=len(x)/2.0	
        fun=lambda x_i: -0.5*((x_i-mean)/self.sigma)**2
        x= [np.exp(fun(x_i)) for x_i in x]
        return x/np.sum(x)

make_plot(proposed)
make_plot(Normal(sigma=3),title='Normal distribution (mean=15,sigma=3)')
make_plot(Normal(sigma=10),title='Normal distribution (mean=15,sigma=10)')