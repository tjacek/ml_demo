import numpy as np
#from scipy.interpolate import CubicSpline
import scipy
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

def get_x(start=0,end=1,n=120):
    step= (end-start)/n
    return np.arange(start=start,
                     stop=end,
                     step=step)

def warp_agum(ts):
    size=len(ts)
    step=1.0/size
    x=np.arange(start=0,
                stop=size)/size
    spline=scipy.interpolate.CubicSpline(x,ts)
   
#    quarter,eight=int(size/4),int(size/8)
    start_x = get_x(start=0,
                    end=0.75,
                    n=105)
    end_x= get_x(start=0.75,
                 end=1.0,
                 n=15)
    new_x=np.concatenate([start_x,end_x])
    new_y=spline(new_x)  
    return get_x(n=120) ,new_y

def apply_fun(fun,
             n_step=200, 
             start= -40.0,
             end= 40.0):
    step=( end-start)/n_step
    x=np.array([ step*i + start for i in range(n_step)])
    ts=[fun(x_i) for x_i in x]
    return x,ts

def plot_fun(*args, **kwargs):
    x,ts=apply_fun(*args, **kwargs)
    plot_ts(x,[ts],name="Szereg czasowy")
    x,ts=warp_agum(ts)
    x=  80*x-40
    plot_ts(x,[ts,ts],name="Augmentowany szereg czasowy")

def plot_ts(x,ts,name):
    fig, ax = plt.subplots()
    plt.figure(figsize=(10,3))
    for ts_i in ts:
        plt.plot(x,ts_i)
    plt.title(name)
    plt.tight_layout()
    plt.show()

def fun(x_i):
    if(np.abs(x_i)<20):
        C=1.0/ np.sqrt(1.0+np.abs(x_i))
    else:
         C=1.0/ (1.0+np.abs(x_i))
    return C*np.sin(x_i) 

plot_fun(fun)