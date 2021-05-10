#import numpy as np
import math
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self,v0,theta,x0,y0,dt,rho,C_d,A,m):
        self.v0=v0
        self.theta=theta
        self.x0=x0
        self.y0=y0
        self.dt=dt
        self.x=x0
        self.y=y0
        self.rho=rho
        self.C_d = C_d
        self.A = A
        self.m=m
        self.x_=[]
        self.y_=[]
        self.x_.append(x0)
        self.y_.append(y0)
        theta=math.radians(self.theta)
        self.vx=self.v0*math.cos(theta)
        self.vy=self.v0*math.sin(theta)

    def reset(self):
        self.v0=0
        self.theta=0
        self.x0=0
        self.y0=0
        self.dt=0
        self.rho=0
        self.C_d = 0
        self.A = 0
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

    def sgn(self,a):
        if a>0:
            return 1
        else:
            return -1
        


    def __move_otpor(self, dt):
        self.dt=dt
        g=9.81
        ax= -((self.rho*self.C_d*self.A)/(2*self.m))*(self.vx)**2
        ay= -g - self.sgn(self.vy)*((self.rho*self.C_d*self.A)/(2*self.m))*(self.vy)**2
        self.x=self.x + self.vx*dt
        self.vx=self.vx + ax*dt
        self.vy=self.vy + ay*dt
        self.y=self.y + self.vy*dt
        self.x_.append(self.x)
        self.y_.append(self.y)

    def range(self):
        while True:
            self.__move_otpor(self.dt)
            if self.y <=0:
                break
        return max(self.x_)
    
    def plot_trajectory(self):
        plt.plot(self.x_,self.y_)
        plt.show()





p1=Projectile(10,45,0,0,0.01,1.22,0.1,0.05,0.1)
p1.range()
p1.plot_trajectory()