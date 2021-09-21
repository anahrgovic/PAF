import matplotlib.pyplot as plt
import Pendulum as pnd

p1=pnd.Pendulum(60,1,0.1,0.01)
p1.oscillate(5)

p2=pnd.Pendulum(1,1,0.1,0.01)
p2.oscillate(5)

plt.figure("pendulum1")
plt.plot(p1.t_,p1.theta_)

plt.figure("pendulum2")
plt.plot(p2.t_,p2.theta_)

plt.show()

#kut otklona unosi se u stupnjevima te se u init funkciji pretvara u radijane
#napravila sam dva grafa, u prvom imamo kut otklona od 60 stupnjeva i on oscilira od -1 do 1, a drugi kut otklona je 1 stupanj i on je od -0.015 do 0.015  