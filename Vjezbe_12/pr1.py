import universe
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



au = 1.496e11
day = 60*60*24
year = 365.242*day

sun = universe.Planet("Sun", 1.989e30, np.array((0.,0.)), np.array((0.,0.)))
mercury = universe.Planet("Mercury",  3.3e24, np.array((0.,0.466*au)), np.array((-47362.0,0.)))

ss = universe.Universe()
ss.add_planet(sun)
ss.add_planet(mercury)
ss.evolve(5.0*year)

plt.style.use('dark_background')
fig = plt.figure()
ax = plt.axes(xlim=(-2e11, 2e11), ylim=(-2e11, 2e11))
ax.set_aspect('equal')
ax.axis('off')
axis.plot(sun.x,sun.y,label=sun.name,color="yellow", linewidth=2.0)
axis.plot(mercury.x,mercury.y,label=mercury.name,color="orange")

# axis.plot(venus.x,venus.y,label=venus.name,color= "red")

# axis.plot(earth.x,earth.y,label=earth.name,color="blue")

# axis.plot(mars.x,mars.y,label=mars.name,color="brown")

lines =[]
planets=[sun, mercury]

for obj in planets:
    line = ax.plot([], [] ,"o")[0]
    lines.append(line)

def init():
    line.set_data([], [])
    return lines

def animate(i):
    x = obj.x[i]
    y = obj.y[i]
    lines[index].set_data(x, y)
    return lines

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(mercury.x), interval=10, blit=True)

plt.show()