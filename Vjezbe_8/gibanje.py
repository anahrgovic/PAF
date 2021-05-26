import projectile as pr
import matplotlib.pyplot as plt

p1 = pr.Projectile(10,45,0,0,0.01,1.22,0.1,0.05,0.1)
xd,yd = p1.evolve()

p2 = pr.Projectile(10,45,0,0,0.01,1.22,0.1,0.05,0.1)
x,y = p2.evolve_RK()

fig= plt.figure(figsize=(20,10))
# x-y graf
plt.plot(xd,yd,label="dt=0.01, Euler")
plt.plot(x,y,label="dt=0.01, Runge-Kutta",c='red')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('x-y graf')
plt.legend(loc="upper right")
plt.savefig("kosi_hitac.pdf")
plt.show()