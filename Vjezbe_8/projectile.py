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
        self.v_x = []
        self.v_y = []
        self.a_x = []
        self.a_y = []
        self.t_=[]
        self.x_.append(x0)
        self.y_.append(y0)
        self.a_x.append(0)
        self.a_y.append(9.81)
        theta=math.radians(self.theta)
        self.vx=self.v0*math.cos(theta)
        self.vy=self.v0*math.sin(theta)
        self.v_x.append(self.vx)
        self.v_y.append(self.vy)
        self.t_.append(0)

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

    def evolve(self):
        while True:
            self.__move_otpor(self.dt)
            if self.y <=0:
                break
        return self.x_,self.y_

    def __a(self, x,v,t):
         return -1*self.sgn(v)*((self.rho*self.C_d*self.A)/(2*self.m))*v**2

    def __move_RK(self, i):
        self.t_.append(self.t_[i-1] + self.dt)

        k1vx = (self.__a(self.x_[i-1], self.v_x[i-1], self.t_[i-1]))*self.dt
        k1vy = (9.81 + self.__a(self.y_[i-1], self.v_y[i-1], self.t_[i-1]))*self.dt
        k1x = self.v_x[i-1] * self.dt
        k1y = self.v_y[i-1] * self.dt

        k2vx = (self.__a(self.x_[i-1]+k1x/2, self.v_x[i-1]+k1vx/2, self.t_[i-1]+self.dt/2))*self.dt
        k2vy = (9.81 + self.__a(self.y_[i-1]+k1y/2, self.v_y[i-1]+k1vy/2, self.t_[i-1]+self.dt/2))*self.dt
        k2x = (self.v_x[i-1]+k1vx/2) * self.dt
        k2y = (self.v_y[i-1]+k1vy/2) * self.dt

        k3vx = (self.__a(self.x_[i-1]+k2x/2, self.v_x[i-1]+k2vx/2, self.t_[i-1]+self.dt/2))*self.dt
        k3vy = (9.81 + self.__a(self.y_[i-1]+k2y/2, self.v_y[i-1]+k2vy/2, self.t_[i-1]+self.dt/2))*self.dt
        k3x = (self.v_x[i-1]+k2vx/2) * self.dt
        k3y = (self.v_y[i-1]+k2vy/2) * self.dt

        k4vx = (self.__a(self.x_[i-1]+k3x/2, self.v_x[i-1]+k3vx/2, self.t_[i-1]+self.dt/2))*self.dt
        k4vy = (9.81 + self.__a(self.y_[i-1]+k3y/2, self.v_y[i-1]+k3vy/2, self.t_[i-1]+self.dt/2))*self.dt
        k4x = (self.v_x[i-1]+k3vx/2) * self.dt
        k4y = (self.v_y[i-1]+k3vy/2) * self.dt

        self.v_x.append(self.v_x[i-1] + (k1vx + 2*k2vx + 2*k3vx + k4vx)/6)
        self.v_y.append(self.v_y[i-1] + (k1vy + 2*k2vy + 2*k3vy + k4vy)/6)

        self.x_.append(self.x_[i-1] + (k1x + 2*k2x + 2*k3x + k4x)/6)
        self.y_.append(self.y_[i-1] + (k1y + 2*k2y + 2*k3y + k4y)/6)
    

    def evolve_RK(self):
        i=0
        while self.y_[i] >= 0:
            self.__move_RK(i)
            i += 1
        return self.x_, self.y_
    
#   def plot_trajectory(self):
        #plt.plot(self.x_,self.y_)
        #plt.show()





#p1=Projectile(10,45,0,0,0.01,1.22,0.1,0.05,0.1)
#p1.range()
#p1.plot_trajectory()