import Particle as prt
import matplotlib.pyplot as plt
import math



dt=0
dt_l=[]
greska_l=[]
N=100

#def pogreska(range,a_domet):
    #ag=math.fabs((p1.range()-p1.a_domet()))/(p1.a_domet())
    #return ag

for i in range(N):
    dt+=0.001
    p1=prt.Particle(10,60,0,0,dt)
    greska=math.fabs((p1.range()-p1.a_domet()))/(p1.a_domet())
    greska_l.append(greska)
    dt_l.append(dt)

plt.xlabel("dt[s]")
plt.ylabel("Absolute relative error [%]")
plt.figure("Absolute relative error for range of projectile")
plt.plot(dt_l,greska_l)
plt.show()

    

