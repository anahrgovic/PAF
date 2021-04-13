import calculus
import math
import matplotlib.pyplot as plt
import numpy as np


#Zadatak 1
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
#print(calculus.deriv(f2,1,0.1))
#print(calculus.derivacija(f2,1,0,0.1))

#print(calculus.deriv(f1,1,0.01))
#print(calculus.deriv(f1,1,0.01))
#print(calculus.derivacija(f1,1,5,0.1))

#a,b=calculus.derivacija(f2,-2,10,0.1)
#plt.plot(xl_,dl_)
#plt.scatter(a,b, s=10, c="r")
#plt.plot(a,b)
#plt.show()


#Zadatak 2

a=0
b=10
def f1(x):
    return 2*x*x-3
def i_f1(x):
    return (2/3)*(x*x*x)-3*x

gornja_l=[]
donja_l=[]
analiticko_r=[]
trapezno=[]
d_l=[]

dx=50
for i in range(1,20):
    d=dx*i
    d_l.append(d)
for d in d_l:
    d_m,g_m=calculus.integr(f1,a,b,d)
    trapez=calculus.integr_tr(f1,a,b,d)
    analit=i_f1(b)-i_f1(a)
    gornja_l.append(g_m)
    donja_l.append(d_m)
    trapezno.append(trapez)
    analiticko_r.append(analit)



#print(calculus.integr(f1,a,b,1))
#print(calculus.integr_tr(f1,a,b,1))
#plt.plot()
#plt.plot(gornja_l,d_l, '.')
plt.plot(donja_l,d_l, '.')
#plt.plot(d_l,trapezno, '.')
plt.plot(d_l,analiticko_r)
plt.show()
