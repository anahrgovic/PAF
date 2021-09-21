import matplotlib.pyplot as plt
import math
import numpy as np

class Pendulum:
    def __init__(self,theta,l,m,dt):
        self.l=l
        self.m=m
        self.theta=theta
        self.__kut(self.theta)
        self.l_=[]
        self.theta_=[]
        self.theta_.append(self.theta)
        self.dt=dt
        self.t=0
        self.t_=[]
        self.t_.append(self.t)
        self.v=0
        #self.k=0


    def __kut(self,theta):
            if theta<=10:
                print('Unesen je mali kut otklona.')


    def change_theta(self, radilist, theta0):
        if radilist == "rad":
            self.theta += theta0
            print("Kut iznosi" ,self.theta, "radijana")
        elif radilist == "deg":
            self.theta += theta0 *math.pi/180
            print("Kut iznosi" ,self.theta * (180/math.pi), "stupnjeva")

    def reset(self):
        del self.theta
        del self.l
        del self.m
        del self.l_
        del self.theta_
        del self.t
        del self.t_


    def __oscillate(self):
        self.a = -9.81 * math.sin(self.theta)
        self.v = self.v + self.a * self.dt
        self.theta = self.theta + self.v * self.dt
        self.t = self.t + self.dt

        self.theta_.append(self.theta)
        self.t_.append(self.t)
    
    def prt(self):
        self.__oscillate()
        print(self.a)
        print(self.v)
        print(self.theta)
        print(self.t)
    
    def oscillate(self, t):
        while self.t <= t:
            self.__oscillate()

        return self.theta_, self.t_
        #print(self.theta_, self.t_)
        #print(f"length of time: {len(self.t_)} ")
        #print(f"length of position: {len(self.theta_)}" )
        


    def oscillate_ar(self, k, t):
        while self.t <= t:
            self.a = - (k * self.v/self.m) - 9.81 * math.sin(self.theta)
            self.v = self.v + self.a * self.dt
            self.theta = self.theta + self.v * self.dt
            self.t = self.t + self.dt
        
            self.theta_.append(self.theta)
            self.t_.append(self.t)

        return self.t_, self.theta_
        #print(self.theta_, self.t_)
        #print(f"length of time: {len(self.t_)} ")
        #print(f"length of position: {len(self.theta_)}" ) 

    
    def period(self):
        T=0
        theta0=self.theta
        while True:
            self.__oscillate()
            T +=self.dt
            if self.theta == theta0:
                break
            elif self.theta == -theta0:
                break
        print(T)
        