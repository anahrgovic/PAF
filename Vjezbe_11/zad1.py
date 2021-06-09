import planeti as grv 
import numpy as np
import math
import matplotlib.pyplot as plt 
dt = (60*60*24)/10
t = 60*60*24*365.242
p1 = grv.Gravity(1.989*10**30, 5.9742*10**24, 6.67408*10**(-11), 0, 0, 1.486*10**11, 0, 0, 0, 0, 29783, dt)
x1,y1,x2,y2 = p1.Euler(t)
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.show()