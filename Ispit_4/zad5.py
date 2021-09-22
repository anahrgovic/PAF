import matplotlib.pyplot as plt
import Pendulum as pnd

p1=pnd.Pendulum(60,1,0.1,0.01)
p1.period()

p1.oscillate(5)
plt.figure("pendulum1")
plt.plot(p1.t_,p1.theta_)
plt.show()

#u 5 zadatku mi računa period do aplitude, stoga u printam 4*T kako bi dobila ukupni period titraja
#napravila sam i graf da možete očitati vrijednost
#T ovisi o l, ako stavimo veći l period će biti veći
