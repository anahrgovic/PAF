
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import universe
#plt.style.use('dark_background')
au = 1.496e11
day = 60*60*24
year = 365.242*day
sun = universe.Planet("Sun", 1.989e30, np.array((0.,0.)), np.array((0.,0.)))
mercury = universe.Planet("Mercury",  3.3e24, np.array((0.,0.466*au)), np.array((-47362.0,0.)))
ss = universe.Universe()
ss.add_planet(sun)
ss.add_planet(mercury)
ss.evolve(3.0*year)

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-2e11, 2e11), ylim=(-2e11, 2e11))
line, = ax.plot([], [] ,lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    x = mercury.x[i]
    y = mercury.y[i]
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(mercury.x), interval=20, blit=True)


#plt.plot(mercury.x[-1],mercury.y[-1],'o',color="orange")
plt.show()