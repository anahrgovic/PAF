import Pendulum as pnd

p1=pnd.Pendulum(5,3,2)
p1.evolve(0.01,3)



p1.plot_trajectory()