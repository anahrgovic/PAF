from numpy.core.records import array
import particl as part
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

def konst_p(t):
    Bx=0
    By=0
    Bz=1
    return np.array((Bx,By,Bz))

def promj_p(t):
    Bx=0
    By=0
    Bz=t/10
    return np.array((Bx,By,Bz))
 

p1=part.particle(np.array((0,0,0)),np.array((0.1,0.1,0.1)),1,-1,konst_p)
x1,y1,z1=p1.evolve_RK(20)
p1.reset()
p1=part.particle(np.array((0,0,0)),np.array((0.1,0.1,0.1)),1,-1,promj_p)
x2,y2,z2=p1.evolve_RK(20)

ax = plt.axes(projection = "3d")
ax.plot3D(x1,y1,z1, c = "blue" )
ax.plot3D(x2,y2,z2, '-.', c = "red")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("usporedba polja")
ax.view_init(30,30)
plt.legend(loc = "upper center")
plt.show()

p2=part.particle(np.array((0,0,0)),np.array((0.1,0.1,0.1)),1,1,promj_p)
x3,y3,z3=p2.evolve_RK(20)


ax = plt.axes(projection = "3d")
ax.plot3D(x1,y1,z1,'-.', c = "blue", label = "elektron")
ax.plot3D(x3,y3,z3, c = "red", label = "pozitron")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.view_init(30,30)
plt.legend()
plt.show()