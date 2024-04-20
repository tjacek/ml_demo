import numpy as np
import matplotlib.pyplot as plt

class LinearFunction(object):
    def __init__(self,a:float,
    	              b:float,
    	              x_label:str,
    	              y_label:str):
        self.a=a
        self.b=b 
        self.x_label=x_label
        self.y_label=y_label


    def __call__(self,p:float):
        return self.b + self.a*p

    def show(self,n=100,step=2):
        fig, ax = plt.subplots()
        x = np.arange(0, n,step=step)
        y= self(x)
        plt.plot(x,y)
        plt.xlabel(self.x_label,fontsize=15) 
        plt.ylabel(self.y_label,fontsize=15) 
        plt.show()
        
class Supply(LinearFunction):
    def __init__(self,a:float,
    	              b:float):
    	super().__init__(a=a,
    	                 b=b,
    	                 x_label="P",
    	                 y_label="X_s")	

class Demand(LinearFunction):
    def __init__(self,a:float,
    	           b:float):
        if(a>0):
            a*= (-1)
        super().__init__(a=a,
    	                 b=b,
    	                 x_label="P",
    	                 y_label="X_s")	 


def inter(start=-10,end=30,step=1):
    d=Demand(-2,60)
    s=Supply(2,-40)
    fig, ax = plt.subplots()
    p = np.arange(start, end,step=step)
    x_s=s(p)
    x_d=d(p)
    plt.plot(p,x_s)
    plt.plot(p,x_d)
    eq_point= p[np.argmin(np.abs(x_s-x_d))]
    plt.axvline(x=eq_point)
    plt.xlabel("P",fontsize=15) 
    plt.ylabel("X",fontsize=15) 
    plt.show()

inter()