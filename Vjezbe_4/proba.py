import calculus
import math
import matplotlib.pyplot as plt


def f1(x):
    return 5*(x**3)-2*(x**2)+2*x-3
def f2(x):
    return x*x-2*x

print(calculus.deriv(f1,1,0.01))
print(calculus.deriv(f1,1,0.01))
print(calculus.derivacija(f1,1,5,0.1))

a,b=calculus.derivacija(f1,-2,2,0.01)
plt.plot(a,b)
plt.show()
