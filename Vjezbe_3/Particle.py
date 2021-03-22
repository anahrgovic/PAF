import matplotlib.pyplot as plt
import math
import numpy as np

class Particle:
    #dt=float(input('Unesi interval promjene vremena:'))
    def __init__(self,v0,theta,x0,y0):
        self.v0=v0
        self.theta=theta
        self.x0=x0
        self.y0=y0
        self.x_=[]
        self.y_=[]
    def printInfo(self):
        print('Čestica je iz početnog položaja ({0:.2f}, {1:.2f}) izbačena početnom brzinom {2:.2f} m/s pod kutom od {3:.2f} stupnjeva.'.format(self.x0,self.y0,self.v0,self.theta))
    def reset(self):
        self.v0=0
        self.theta=0
        self.x0=0
        self.y0=0
    def __move(self, dt):
        self.dt=dt
        g=9.81
        y=self.y0
        x=self.x0
        theta=np.radians(self.theta)
        vx=self.v0*math.cos(theta)
        vy=self.v0*math.sin(theta)
        vy=vy - g*dt
        x=x+ vx*dt
        y=y+ vy*dt
        self.x_.append(x)
        self.y_.append(y)
    def evolve(self,t):
        for i in range(t):
            self.__move(0.01)
    #def range(self,dt):
      
        #while True:
           
           # y=self.y0+ vy*dt
            #if y<0:
             #   break 
    def plot_trajectory(self):
        plt.plot(self.x_,self.y_)

           
        
        


        


p1=Particle(10,45,3,5)
p1.printInfo()
#p1.reset()
print(p1.v0,p1.theta,p1.x0)
p1.evolve(10)
print(p1.x_)

