import matplotlib.pyplot as plt
import Pendulum as pnd

p1=pnd.Pendulum(5,1,0.1)
p1.evolve(0.01,5)

plt.figure("pendulum")
plt.plot(p1.t_,p1.l_)
plt.show()
