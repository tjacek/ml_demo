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
    	              series:Series,
    	              name:str):
        self.params=params
        self.series=series
        self.name=name

    def x_value(self):
    	return self.series.y

class IS(Variable):
    def __call__(self):
    	 value=  self.params.c*(1 - self.params.t)
    	 value= (self.params.A - self.series.y*value)/self.params.b        
    	 return value

class LM(Variable):
    def __call__(self):
        return (1/self.params.h)*(self.params.k* self.series.y - self.params.Ms/self.params.P)

class AD(Variable):
    def __call__(self):
       value=(self.series.y*(1- self.params.c*(1-self.params.t)+self.params.b/self.params.h*self.params.k) - self.params.A)
       value= self.params.b/self.params.h*self.params.Ms/value 
       return value	

class Y_EQ(Variable):
    def __init__(self,params:Parameters,
    	              series:Series):
        super().__init__(params=params,
    	                 series=series,
    	                 name="Y_EQ")
        self.is_curve=IS(params=params,
    	                 series=series,
    	                 name="IS")
        self.lm_curve=LM(params=params,
    	                 series=series,
    	                 name="LM")
    def __call__(self):
        diff=np.diff(np.sign(self.is_curve() - self.lm_curve()))
        return np.argwhere(diff).flatten()

class I_EQ(Variable):
    def __init__(self,params:Parameters,
    	              series:Series):
        super().__init__(params=params,
    	                 series=series,
    	                 name="I_EQ")
        self.y_eq=IS(params=params,
    	             series=series,
    	             name="I_EQ")

    def __call__(self):
        return (1/self.params.h)*(self.params.k* self.y_eq() - self.params.Ms/self.params.P)

class AE(Variable):
    def __init__(self,params:Parameters,
    	              series:Series):
        super().__init__(params=params,
    	                 series=series,
    	                 name="AE")
        self.i_eq=I_EQ(params=params,
    	               series=series)   

    def __call__(self):
       value=self.params.A
       value+=self.params.c*(1-self.params.t)*self.series.y
       value-= self.params.b*self.i_eq() 
       return value

# A + c*(1-t)*y - b*i_eq()

def MD():
    M = np.arange(0, 50000)
    return (1/h)*(k*y_eq() - M)


def show_curves(curves,x_label='Y',y_label='i'):
    fig, ax = plt.subplots()
    
    for curve_i in curves:
        plt.plot(curve_i.x_value(),
        	     curve_i(),
        	     label=curve_i.name)
    plt.xlabel(x_label,fontsize=15) 
    plt.ylabel(y_label,fontsize=15) 
    plt.legend()
    plt.tight_layout()
    plt.show()


params=Parameters()
series=Series()

is_curve=IS(params=params,
	        series=series,
	        name="IS")
lm_curve=LM(params=params,
	        series=series,
	        name="LM")

show_curves(curves=[is_curve,lm_curve],
	        x_label='Y',
	        y_label='i')

ad=AE(params=params,
	  series=series)
show_curves(curves=[ad],
	        x_label='Y',
	        y_label='AD')