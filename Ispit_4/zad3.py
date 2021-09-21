import matplotlib.pyplot as plt
import Pendulum as pnd

p1=pnd.Pendulum(0.01,1,0.1,0.01)
p1.oscillate(5)

plt.figure("pendulum")
plt.plot(p1.t_,p1.theta_)
plt.show()