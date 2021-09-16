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
        self.k=0


    def __kut(self,theta):
            if theta<=10:
                print('Unesen je mali kut otklona.')


    def change_theta(self, radilist, theta):
        self.theta = theta
        if radilist == "rad":
            print("Kut iznosi" ,self.theta, "radijana")
        elif radilist == "deg":
            print("Kut iznosi" ,self.theta, "stupnjeva")
            self.theta = self.theta*math.pi/180
    

    def reset(self):
        del self.theta
        del self.l
        del self.m
        del self.l_
        del self.theta_

    def __oscillate(self):
        self.a = -9.81 * math.sin(self.theta)
        self.v = self.v + self.a * self.dt
        self.theta = self.theta + self.v * self.dt
        self.t = self.t + self.dt

        self.theta_.append(self.theta)
        self.t_.append(self.t)


    def oscillate(self, t):
        while self.t <= t:
            self.__oscillate()

        return self.theta_, self.t_
        #print(self.theta_, self.t_)
        #print(f"length of time: {len(self.t_)} ")
        #print(f"length of position: {len(self.theta_)}" )
        


    def oscillate_ar(self, k, t):
        while self.t <= t:
            self.a = ((self.k * self.v) / self.m -9.81) * math.sin(self.theta)
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
        T=2*math.pi*math.sqrt(self.l/9.81)
        print(T)
        