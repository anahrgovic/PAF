import calculus
import math
import matplotlib.pyplot as plt
import numpy as np



def f1(x):
    return 5*(x**3)-2*(x**2)+2*x-3
x1_=-2
x2_=2
h_=0.01
xl_=np.arange(x1_,x2_,h_)
dl_=[]
for x in xl_:
    d=15*(x**2)-4*x+2
    dl_.append(d)

def f2(x):
    return math.sin(x)
print(calculus.deriv(f2,1,0.1))
print(calculus.derivacija(f2,1,0,0.1))

#print(calculus.deriv(f1,1,0.01))
#print(calculus.deriv(f1,1,0.01))
#print(calculus.derivacija(f1,1,5,0.1))

a,b=calculus.derivacija(f2,-2,10,0.1)
#plt.plot(xl_,dl_)
plt.scatter(a,b, s=10, c="r")
#plt.plot(a,b)
plt.show()
