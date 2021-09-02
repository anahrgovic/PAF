import matplotlib.pyplot as plt
import Pendulum as pnd

p1=pnd.Pendulum(5,1,0.01)
p1.run_event_with_ar(0.05,1)


plt.figure("pendulum")
plt.plot(p1.t_,p1.l_)
plt.show()