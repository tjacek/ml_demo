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
         self.P = 1

class Series(object):
    def __init__(self,n=100000):
        self.y = np.arange(100000)	
        self.M = np.arange(50000)


class Variable(object):
    def __init__(self,params:Parameters,
    	              series:Series):
        self.params=params
        self.series=series

class IS(Variable):
    def __call__(self):
    	 value=  self.params.c*(1 - self.params.t)
    	 value= (self.params.A - self.series.y*value)/self.params.b        
#    	 raise Exception(value.shape)
    	 return value

class LM(Variable):

    def __call__(self):
        return (1/self.params.h)*(self.params.k* self.series.y - self.params.Ms/self.params.P)

def MD():
    M = np.arange(0, 50000)
    return (1/h)*(k*y_eq() - M)

def y_eq():
    return np.argwhere(np.diff(np.sign(IS() - LM()))).flatten()

def show_curves(curves,x_label='Y',y_label='i'):
    fig, ax = plt.subplots()
    
    for curve_i in curves:
        plt.plot(curve_i.series.y,curve_i()) #,label="lsm")
    plt.xlabel(x_label,fontsize=15) 
    plt.ylabel(y_label,fontsize=15) 
#    plt.legend()
    plt.tight_layout()
    plt.show()


params=Parameters()
series=Series()

is_curve=IS(params=params,series=series)
lm_curve=LM(params=params,series=series)

show_curves(curves=[is_curve,lm_curve],
	        x_label='Y',
	        y_label='i')