import numpy as np
import matplotlib.pyplot as plt


class Parameters(object):
    def __init__(self):
         self.A=2700
         self.b=18000
         self.c=0.8
         self.t=0.2
         self.h=180000
         self.k=0.34
         self.Ms = 8000 
         self.p = 1

class Series(object):
    def __init__(self,n=100000):
        self.y = np.arange(100n000)	
        self.M = np.arange(0, 50000)

def IS():
    return (A - y*(1 - c*(1 - t)))/b

def LM():
    return (1/h)*(k*y - Ms/P)

def MD():
    M = np.arange(0, 50000)
    return (1/h)*(k*y_eq() - M)

def y_eq():
    return np.argwhere(np.diff(np.sign(IS() - LM()))).flatten()

def show_curves():
    fig, ax = plt.subplots()
    ts=[[1,2,3,4,5],
        [1,4,9,16,25]]
    plt.plot(ts[0],ts[1]) #,label="lsm")
    plt.xlabel("Y",fontsize=15) 
    plt.ylabel("i",fontsize=15) 
#    plt.legend()
    plt.tight_layout()
    plt.show()

show_curves()