import numpy as np
import matplotlib.pyplot as plt


def show_plot(x,ts):
    fig, ax = plt.subplots()
    plt.figure(figsize=(10,3))
    for ts_i in ts:
        plt.plot(x,ts_i)
    plt.tight_layout()
    plt.show()

def fun1(x):
    return np.array([ np.cos((x_i-5)**2) for x_i in x])	

def fun2(x):
    t=[ np.cos(x_i) for x_i in x]
    return np.array([ (t-5)**2 for t_i in t]) 


x=np.arange(100,step=1)
y1=np.sin(x)#/10)
y2=fun1(x)
y3=np.log(x)/2
print(x)
show_plot(x,[y1,y2,y3])