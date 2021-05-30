import particle as part
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

p1=part.particle(np.array((0,0,0)),np.array((0,0,1)),np.array((0.1,0.1,0.1)),1,1)
p1.euler(20)

p2=part.particle(np.array((0,0,0)),np.array((0,0,1)),np.array((0.1,0.1,0.1)),1,-1)
p2.euler(20)

ax = plt.axes(projection = "3d")

ax.plot3D(p2.r_x,p2.r_y,p2.r_z, c = "blue", label = "elektron")
ax.plot3D(p1.r_x,p1.r_y,p1.r_z, c = "red", label = "pozitron")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.view_init(30,30)
plt.legend()
plt.show()