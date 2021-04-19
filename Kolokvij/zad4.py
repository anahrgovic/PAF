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
        self.t_=[]
        self.vy=self.vy - g*dt
        self.h=self.h0 + self.vy*dt
        self.t += dt
        self.h_.append(self.h)
        self.v_.append(self.vy)
        self.t_.append(self.t)
        return self.h_,self.v_,self.t_

    def gibanje(self):
        while True:
            self.izrac_vh(self.t)
            if self.h <=0:
                break
        print(max(self.h_))
        #return max(self.h_)


vh1=Vertikalnihitac(10,10)
vh1.izrac_vh(10)
vh1.gibanje()

