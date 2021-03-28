import matplotlib.pyplot as plt
import math
import numpy as np

class Particle:
    def __init__(self,v0,theta,x0,y0,dt):
        self.v0=v0
        self.theta=theta
        self.x0=x0
        self.y0=y0
        self.dt=dt
        self.x=x0
        self.y=y0
        self.x_=[]
        self.y_=[]
        self.x_.append(x0)
        self.y_.append(y0)
        theta=np.radians(self.theta)
        self.vx=self.v0*math.cos(theta)
        self.vy=self.v0*math.sin(theta)

    def printInfo(self):
        print('Čestica je iz početnog položaja ({0:.2f}, {1:.2f}) izbačena početnom brzinom {2:.2f} m/s pod kutom od {3:.2f} stupnjeva.'.format(self.x0,self.y0,self.v0,self.theta))
    
    def reset(self):
        self.v0=0
        self.theta=0
        self.x0=0
        self.y0=0
        self.dt=0
        self.x_=[]
        self.y_=[]
        
        
    def __move(self, dt):
        self.dt=dt
        g=9.81
        self.x=self.x + self.vx*dt
        self.vy=self.vy - g*dt
        self.y=self.y + self.vy*dt
        self.x_.append(self.x)
        self.y_.append(self.y)

    def evolve(self,t):
        for i in range(t):
            self.__move(self.dt)

    def range(self):
        while True:
            self.__move(self.dt)
            if self.y <=0:
                break

    def plot_trajectory(self):
        plt.plot(self.x_,self.y_)
        plt.show()

    def a_domet(self):
        g=9.81
        d=((self.v0)**2 * math.sin(2*self.theta))/g
        return d

p1=Particle(10,60,0,0,0.01)
#p1.printInfo()
#print(p1.v0,p1.theta,p1.x0)
#p1.reset()
#p1.evolve(10)
#p1.range()
#print(p1.x_)
#p1.plot_trajectory()
print(p1.a_domet())