import calculus 
import math
import numpy as np

def f1(x):
    return 5*(x**3)-2*(x**2)+2*x-3

print(calculus.derivacija(f1,1,5,0.1))