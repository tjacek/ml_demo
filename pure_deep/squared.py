import numpy as np
import matplotlib.pyplot as plt

def show_plot(n=30):
    names=range(n)
    values=get_dist(n)
    plt.bar(names, values)
    plt.xlabel('frames')
    plt.ylabel('probability')    
    plt.show()

def get_dist(n):
    inc,dec=np.arange(n),np.flip(np.arange(n))
    dist=np.amin(np.array([inc,dec]),axis=0)
    dist=dist.astype(float)
    dist=dist**2
    dist/=np.sum(dist)
    return dist

show_plot(n=30)