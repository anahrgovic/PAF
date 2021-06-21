import universe
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
au = 1.496e11
day = 60*60*24
year = 365.242*day

sun = universe.Planet("Sun", 1.989e30, 0.696e9 ,np.array((0.,0.)), np.array((0.,0.)))
earth = universe.Planet("Earth", 5.9742e24,0.637e6, np.array((-1*au,0.)), np.array((0.,29783.)))
mercury = universe.Planet("Mercury", 3.3e24, 2.439e6,np.array((0,0.466*au)), np.array((-47362.,0.)))
venus = universe.Planet("Venus", 4.8685e24,6.371e6, np.array((0.723*au,0.)), np.array((0.,35020.)))
mars = universe.Planet("Mars", 6.417e23, 3.389e6, np.array((0.,-1.666*au)), np.array((24007.,0.)))
comet = universe.Planet("comet", 1e14, 0.5e3, np.array((4.*au,4*au)), np.array((-20000.,-15000.)))
ss = universe.Universe()
ss.add_planet(sun)
ss.add_planet(earth)
ss.add_planet(mercury)
ss.add_planet(venus)
ss.add_planet(mars)
ss.add_planet(comet)


ss.evolve(5.0*year)

fig= plt.figure(figsize=(10,10))
plt.plot(sun.x,sun.y,label=sun.name,color="yellow", linewidth=5.0)
plt.plot(earth.x,earth.y,label=earth.name,color="blue")
plt.plot(mars.x,mars.y,label=mars.name,color="red")
plt.plot(mercury.x,mercury.y,label=mercury.name,color="orange")
plt.plot(venus.x,venus.y,label=venus.name,color="green")
plt.scatter(earth.x[-1],earth.y[-1])
plt.scatter(mercury.x[-1],mercury.y[-1])
plt.scatter(venus.x[-1],venus.y[-1])
plt.scatter(mars.x[-1],mars.y[-1])

plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y graf')
plt.legend(loc="upper right")
plt.show()

fig,ax = plt.figure(figsize=(10, 10)), plt.axes(xlim=(-10e11, 10e11), ylim=(-10e11, 10e11))

line, = ax.plot([], [],'o',color="yellow")
line1, = ax.plot([], [],'o',color="blue")
line2, = ax.plot([], [], 'o',color="orange")
line3, = ax.plot([], [], 'o',color="green")
line4, = ax.plot([], [], 'o',color="red")
line5, = ax.plot([], [], 'o',color="black")

xe, ye = [], []
xs, ys = [], []
xmar,ymar = [],[]
xmer, ymer = [],[]
xv,yv = [], []
xc,yc = [], []
def init():
    line.set_data([],[])
    line1.set_data([],[])
    line2.set_data([],[])
    line3.set_data([],[])
    line4.set_data([],[])
    line5.set_data([],[])
    return line,line1,line2,line3,line4,line5

def animate(i):
    xs.append(sun.x[i])
    ys.append(sun.y[i])
    xe.append(earth.x[i])
    ye.append(earth.y[i])
    ymer.append(mercury.y[i])
    xmer.append(mercury.x[i])
    xv.append(venus.x[i])
    yv.append(venus.y[i])
    xmar.append(mars.x[i])
    ymar.append(mars.y[i])
    xc.append(comet.x[i])
    yc.append(comet.y[i])

    line.set_data(xs[i],ys[i])
    line1.set_data(ye[i],xe[i])
    line2.set_data(xmer[i],ymer[i])
    line3.set_data(xv[i],yv[i])
    line4.set_data(xmar[i],ymar[i])
    line5.set_data(xc[i],yc[i])
    

    return line,
plt.plot(sun.x,sun.y,label=sun.name,color="yellow", linewidth=5.0)
plt.plot(earth.x,earth.y,label=earth.name,color="blue")
plt.plot(mars.x,mars.y,label=mars.name,color="red")
plt.plot(mercury.x,mercury.y,label=mercury.name,color="orange")
plt.plot(venus.x,venus.y,label=venus.name,color="green")
plt.plot(comet.x,comet.y,label=comet.name,color="black")
anim = animation.FuncAnimation(fig, animate, init_func=init, interval=1)
plt.show()