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
    return [min(d(start,i),d(i,end)) for i in x]

def d(i,j):
    return np.abs(i-j)	

class Normal(object):
    def __init__(sigma):
        self.sigma=sigma	

make_plot(proposed)