from supply import LinearFunction,Demand
import numpy as np
import matplotlib.pyplot as plt


d=Demand(-2,60)
#d.show()
p = np.arange(0, 30,step=1)

el=[ d.diff(p_i)*(p_i/d(p_i)) for p_i in p]

fig, ax = plt.subplots()
plt.plot(p,el)
plt.plot(p,d(p))
plt.plot(p,[-1.0 for p_i in p])
plt.show()