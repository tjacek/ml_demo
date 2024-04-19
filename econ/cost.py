import numpy as np
import matplotlib.pyplot as plt

class Cost(object):
    def TC(self,x:float):
        return self.TFC(x) + self.TVC(x)

    def TFC(self,x:float):
        raise NotImplementedError()

    def TVC(self,x:float):
        raise NotImplementedError()

    def ATC(self,x:float):
        return self.TC(x)/x

    def AVC(self,x:float):
        return self.TVC(x)/x

    def AFC(self,x:float):
        return self.TFC(x)/x	


class Zad1(Cost):
    def TFC(self,x:float):
        return x*(1.5*x*x -6*x+36)

    def TVC(self,x:float):
        return 30

def show_series(fun,start=-150,end=100,step=1):
    n= int((end-start)/step)
    x = np.arange(0, n,step=step)+start
#    y=np.array([ fun(x_i) for x_i in x])
    y=fun(x)
    print(y.shape)
    show_plot(x,y)

def show_plot(x,y):
    fig, ax = plt.subplots()
#    plt.figure(figsize=(10,3))
#    for ts_i in ts:
    plt.plot(x,y)
    plt.tight_layout()
    plt.show()

zad1=Zad1()

show_series(lambda x:zad1.TC(x))
