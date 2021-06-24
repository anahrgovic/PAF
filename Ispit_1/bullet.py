import matplotlib.pyplot as plt
import math
import numpy as np

class Bullet:
    def __init__(self,v0,y0,dt,l,rho,C_d,A,):
        self.v0=v0
        self.y0=y0
        self.t=0
        self.dt=dt
        self.l=l
        self.y_=[]
        self.v_=[]
        self.t_=[]
        self.x_=[]
        self.y_.append(self.y0)
        self.v_.append(self.v0)
        self.t_.append(self.t)
        self.x_.append(self.l)

    def __printInfo(self):
         print('Objekt je uspješno stvoren. Početna brzina objekta je {0:.2f} m/s, početna visina je {1:.2f} m.'.format(self.v0,self.y0))

    def ispis(self):
        self.__printInfo()

    def change_v0(self,v):
        self.v0+=v

    def change_y0(self,y):
        self.y0+=y    

    def printInfo2(self):
        print('Nova početna brzina objekta je {0:.2f} m/s, nova početna visina je {1:.2f} m.'.format(self.v0,self.y0))

    def reset(self):
        del self.v0
        del self.y0
        del self.t
        del self.dt
        del self.l
        del self.y_
        del self.v_
        del self.t_
        del self.x_

    def __move(self, dt, theta=0):
        self.dt=dt
        g=9.81
        self.vx=self.v0*math.cos(theta)
        self.vy=self.v0*math.sin(theta)
        self.t+=dt
        self.l=self.l + self.vx*dt
        self.v=self.vy - g*dt
        self.y=self.y0 + self.v*dt
        self.y_.append(self.y)
        self.t_.append(self.t)
        self.x_.append(self.l)
        #print(self.y_,self.x_,self.t_)

    def evolve(self,t):
        for i in range(t):
            self.__move(self.dt)

    def range(self):
        while True:
            self.__move(self.dt)
            if self.y <=0:
                break
        print(self.y_) 
        

    def sgn(self,a):
        if a>0:
            return 1
        else:
            return -1
        
    def __move_otpor(self, dt):
        self.dt=dt
        g=9.81
        ay= -g - self.sgn(self.vy)*((self.rho*self.C_d*self.A)/(2*self.m))*(self.vy)**2
        self.l=self.l + self.vx*dt
        self.vx=self.vx + ax*dt
        self.vy=self.vy + ay*dt
        self.y=self.y + self.vy*dt
        self.x_.append(self.l)
        self.y_.append(self.y)

    def evolve2(self):
        while True:
            self.__move_otpor(self.dt)
            if self.y <=0:
                break
        return self.x_,self.y_
        
        

    