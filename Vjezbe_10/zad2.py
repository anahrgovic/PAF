import particle as part
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

p1=part.particle(np.array((0,0,0)),np.array((0,0,1)),np.array((0.1,0.1,0.1)),1,-1)
x1,y1,z1=p1.euler(20)
p1.reset()
p1=part.particle(np.array((0,0,0)),np.array((0,0,1)),np.array((0.1,0.1,0.1)),1,-1)
x2,y2,z2=p1.evolve_RK(20)

ax = plt.axes(projection = "3d")
ax.plot3D(x1,y1,z1, c = "blue", label = "Euler, dt = 0.01")
ax.plot3D(x2,y2,z2, '-.', c = "blue", label = "Runge-Kutta, dt = 0.01")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.view_init(30,-60)
plt.legend()
plt.show()