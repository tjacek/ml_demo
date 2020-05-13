import numpy as np
import matplotlib.pyplot as plt

def show_plot(n=30):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    x = range(n)
    y = get_dist(n)
    ax.bar(x,y)
    plt.show()

def get_dist(n):
    inc,dec=np.arange(n),np.flip(np.arange(n))
    dist=np.amin(np.array([inc,dec]),axis=0)
    dist=dist.astype(float)
    dist=dist**2
    dist/=np.sum(dist)
    return dist

show_plot(n=30)