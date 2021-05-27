import numpy as np
import matplotlib.pyplot as plt

class particle:
    def __init__(self,E,B,v,m,q,dt=0.01):
        self.E=E
        self.B=B
        self.v=v
        self.m=m
        self.q=q
        self.dt=dt
        self.r = np.array((0,0,0))
        self.r_ = []

    def reset(self):
        del self.E
        del self.B
        del self.v
        del self.m
        del self.q
        del self.dt

    def move(self):
        a = (self.q/self.m)*(self.E+ np.cross(self.v,self.B))
        self.v = self.v + a*self.dt
        self.r = self.r + self.v*self.dt
        self.r_.append(self.r)
        print(a,self.v,self.r)

p1=particle(np.array((0,0,0)),np.array((0,0,1)),np.array((0.1,0.1,0.1)),1,1)
p1.move()
      

