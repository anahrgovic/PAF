import math
import matplotlib.pyplot as plt

class BungeeJumping:
    def __init__(self,m,k,v0,h0,l,rho=1,Cd=1,A=1,dt=0.01,AirResistance = False):
        self.m=m 
        self.k=k
        self.l=l
        self.h0=h0
        self.rho=rho 
        self.Cd=Cd
        self.A=A
        self.dt=dt
        self.AirResistance=AirResistance
        self.h=h0
        self.v0=0 
        self.t=0 
        self.h_=[]
        self.t_=[]
        self.h_.append(self.h)
        self.t_.append(self.t)
        self.U=self.m * 9.81 * self.h
        self.K=0 
        self.Ee=0
        self.E = self.U + self.K + self.Ee
        self.U_= []
        self.K_ = []
        self.Ee_ = []
        self.E_ = []
        self.U_.append(self.U)
        self.K_.append(self.K)
        self.Ee_.append(self.Ee)
        self.E_.append(self.E)

    def reset(self):
        del self.m 
        del self.k
        del self.l
        del self.h0
        del self.rho
        del self.Cd
        del self.A
        del self.dt
        del self.AirResistance
        del self.h
        del self.v0
        del self.t 
        del self.h_
        del self.t_
        del self.U
        del self.K 
        del self.Ee
        del self.E
        del self.U_
        del self.K_
        del self.Ee_
        del self.E_

    def akceleracija(self):
        dh = self.h0 - self.l - self.h
        if dh > 0:
            akc_el = (self.k/self.m)*dh
        else: 
            akc_el = 0
        if self.AirResistance:
            akc_AR = -(abs(self.v)*self.v0*self.rho*self.Cd*self.A)/(2*self.m)
        else:
            akc_AR = 0
        a = -9.81 + akc_el + akc_AR
        return a

    def energija(self):
        dh = self.h0 - self.l - self.h
        if dh > 0:
            self.Eel = (1/2)*self.k*dh*dh
        #else:
        #    E = 0
        #return E
    
    def __skok(self):
        self.a = self.akceleracija()
        self.v0 += self.a*self.dt
        self.h += self.v0*self.dt
        self.t += self.dt
        self.energija()

    def skok(self,t):
        while self.t < t:
            self.__skok()
            self.h_.append(self.h)
            self.t_.append(self.t)
            self.Ee_.append(self.Ee)
            self.K_.append(self.K)
            self.U_.append(self.U)
            self.E_.append(self.E)
    
BJ=BungeeJumping(100,20,0,250,50,False)
BJ.skok(50)

plt.figure("Bungee jumping", figsize=(15, 10), dpi=80)
fig = plt.subplot()

plt.subplot(2,2,1)
plt.plot(BJ.t_,BJ.h_)
plt.xlabel("t [s]")
plt.ylabel("x [m]")
plt.title("Graf bez otpora zraka")
#plt.show()

plt.subplot(2,2,2)
plt.plot(BJ.t_, BJ.E_, label = "ukupna energija")
plt.plot(BJ.t_, BJ.K_, label = "kineticka energija")
plt.plot(BJ.t_, BJ.U_, label = "potencijalna energija")
plt.plot(BJ.t_, BJ.Ee_, label = "elasticna energija")
plt.title("Energija bez otpora zraka")
plt.legend(loc = "upper right", prop={'size': 10} )
#plt.show()

BJ.reset()

BJ=BungeeJumping(100,20,0,250,50)    
BJ.skok(50)

plt.subplot(2,2,3)
plt.plot(BJ.t_,BJ.h_)
plt.xlabel("t [s]")
plt.ylabel("x [m]")
plt.title("Graf s otporom zraka")
#plt.show()

plt.subplot(2,2,4)
plt.plot(BJ.t_, BJ.E_, label = "ukupna energija")
plt.plot(BJ.t_, BJ.K_, label = "kineticka energija")
plt.plot(BJ.t_, BJ.U_, label = "potencijalna energija")
plt.plot(BJ.t_, BJ.Ee_, label = "elasticna energija")
plt.title("Energija s otporom zraka")
plt.legend(loc = "upper right", prop={'size': 10} )
plt.show()