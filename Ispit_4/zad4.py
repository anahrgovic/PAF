import matplotlib.pyplot as plt
import Pendulum as pnd

p1=pnd.Pendulum(5,1,0.1,0.05)
x1,y1=p1.oscillate_ar(1,5)

p2=pnd.Pendulum(5,1,0.1,0.01)
x2,y2=p2.oscillate(5)

plt.figure("pendulum")
plt.plot(p1.t_,p1.theta_)
plt.plot(p2.t_,p2.theta_)
plt.show()