import numpy as np
import matplotlib.pyplot as plt

def ts(n):
	x=np.arange(n,step=0.1)+1
	y=[np.sin( (0.1*x_i)**2+10)/(x_i+10) for x_i in x]
	return x,np.array(y)

def shapelet(x,y,start=60,step=80):
    s_x=x[start:start+step]
    s_y=y[start:start+step]
    return s_x,1.0*s_y

def shapelet_plot(ts,s):
    fig, ax = plt.subplots()
    plt.rcParams.update({'font.size': 15})
    plt.tick_params(axis='both', which='major', labelsize=15)
    wi, hi = fig.get_size_inches()
    fig.set_size_inches(1.6*wi, hi)
    ax.set_title(f'Przykładowy podciąg Shapelet')
    plt.plot(ts[0],ts[1],label="Szereg czasowy")
    plt.plot(s[0],s[1],label="Podciąg Shapelet")
    plt.legend()
    plt.tight_layout()
    plt.show()

def distance_plot(ts,s):
    s_size=len(s[0])
    n=len(ts[0])-s_size
    dist=[]
    for i in range(n):
        y_i=ts[1][i:i+s_size]
        dist.append(np.linalg.norm(s[1]-y_i)) 
    fig, ax = plt.subplots()
    wi, hi = fig.get_size_inches()
    fig.set_size_inches(1.6*wi, hi)
    plt.rcParams.update({'font.size': 15})
    plt.tick_params(axis='both', which='major', labelsize=15)
    ax.set_title(f'Odległość szeregu czasowego od podciągu Shapelet')
    plt.tight_layout()
    plt.plot(ts[0][:n],dist)
    plt.show()

ts=ts(40)
s=shapelet(*ts)
shapelet_plot(ts,s)
distance_plot(ts,s)