import matplotlib.pyplot as plt
import Pendulum as pnd

p1=pnd.Pendulum(60,1,0.1,0.05)
x1,y1=p1.oscillate_ar(3,5)

p2=pnd.Pendulum(60,1,0.1,0.01)
x2,y2=p2.oscillate(5)

plt.figure("pendulum1")
plt.plot(p1.t_,p1.theta_, "blue")
plt.plot(p2.t_,p2.theta_, "orange")

p3=pnd.Pendulum(5,1,0.1,0.05)
x3,y3=p3.oscillate_ar(0.1,5)

p4=pnd.Pendulum(5,1,0.1,0.01)
x4,y4=p4.oscillate(5)

plt.figure("pendulum2")
plt.plot(p3.t_,p3.theta_, "blue")
plt.plot(p4.t_,p4.theta_, "orange")

plt.show()

#napravila sam 2 grafa u prvom je njihalo s većim kutem otklona i k je jednak 3
#u drugom je manji kut, k je isto manji iznosi 0.1, vidljivo je gušenje