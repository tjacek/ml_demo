import numpy as np
import matplotlib.pyplot as plt

def make_plot(fun=None,n_frames=30,title='dist',outpath=None):
    x=np.arange(n_frames)
    if(fun is None):
        y=x
    else:
    	y=fun(x)
    plt.clf()
    plt.bar(x, y) #color ='maroon',width = 0.4)
    plt.xlabel("Mapa głębi")
    plt.ylabel("Prawdopodobieństwo wylosowania \n mapy głębi")
    plt.title(title)
    fig = plt.gcf()
    fig.set_size_inches(7.5, 3.5)
    plt.tight_layout()
    if(outpath):
        plt.savefig(outpath)
    else:
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

make_plot(proposed,
          title='Proponowany rozkład prawdopodobieństwa',
          outpath='../proposed.png')
make_plot(Normal(sigma=3), 
          title='Rozkład normalny (średnia=15,wariancja=3)',
          outpath='../norm1.png')
make_plot(Normal(sigma=10),
          title='Rozkład normalny (średnia=15,wariancja=10)',
          outpath='../norm2.png')
