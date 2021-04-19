import matplotlib.pyplot as plt
import math
import numpy as np

class Vertikalnihitac:
    def __init__(self,vy0,h0):
        self.vy0=vy0
        self.h0=h0
        self.h_=[]
        self.v_=[]
        self.h_.append(h0)
        self.v_.append(vy0)
        self.vy=self.vy0

    def izrac_vh(self,t):
        self.t=t
        dt=0.01
        g=9.81
        N=2*t
        for i in range(N):
            self.t_=[]
            self.vy=self.vy - g*dt
            self.h=self.h0 + self.vy*dt
            self.t += dt
            self.h_.append(self.h)
            self.v_.append(self.vy)
            self.t_.append(self.t)
        return self.h_,self.v_,self.t_
            
    def plot_trajectory(self):
        plt.plot(self.v_,self.h_)
        plt.show()
        
vh1=Vertikalnihitac(10,10)
vh1.izrac_vh(5)
vh1.plot_trajectory()