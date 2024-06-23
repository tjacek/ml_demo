import numpy as np
import matplotlib.pyplot as plt


def plot_fun(fun,
             n_step=100, 
             start= -35.0,
             end= 35.0):
    step=( end-start)/n_step
    x=np.array([ step*i + start for i in range(n_step)])
    ts=[fun(x_i) for x_i in x]
    plot_ts(x,[ts])

def plot_ts(x,ts):
    fig, ax = plt.subplots()
    plt.figure(figsize=(10,3))
    for ts_i in ts:
        plt.plot(x,ts_i)
    plt.tight_layout()
    plt.show()

def fun(x_i):
    if(np.abs(x_i)<20):
        C=1.0/ np.sqrt(1.0+np.abs(x_i))
    else:
         C=1.0/ (1.0+np.abs(x_i))
    return C*np.sin(x_i) 

#def fun2(x):
#    t=[ np.cos(x_i/3) for x_i in x]
#    return np.array([ (t_i-5)**2 for t_i in t])

plot_fun(fun)