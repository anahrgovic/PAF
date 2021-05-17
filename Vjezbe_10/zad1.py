import numpy as np
import matplotlib.pyplot as plt

E=np.array((0,0,0))
B=np.array((0,0,1))
v=np.array((0.1,0.1,0.1))
q=1
m=1
x=q/m
vp=np.cross(B,v)
c = np.dot(x,E)
print(c)
print(vp)
#print(a[0])