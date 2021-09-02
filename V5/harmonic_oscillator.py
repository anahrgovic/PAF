import math 
import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self,k,m,A,v0):
        self.k=k
        self.m=m
        self.x=A
        self.v=v0
        self.a=-(self.k * self.x)/self.m
        self.t=0
        self.xlist=[]
        self.vlist=[]
        self.alist=[]
        self.tlist=[]
    
    def oscillate(self,dt,t):
        N=int(t/dt)
        for i in range(N):
            self.t +=dt
            self.a=-(self.k * self.x)/self.m
            self.v=self.v + self.a*dt
            self.x=self.x + self.v*dt
            self.xlist.append(self.x)
            self.vlist.append(self.v)
            self.alist.append(self.a)
            self.tlist.append(self.t)
        return self.xlist,self.vlist,self.alist,self.tlist

p1=HarmonicOscillator(0.1,10,0.3,3)
#print(p1.oscillate)
print(p1.xlist)
print(p1.oscillate(0.01,2))
print(p1.v)

print(p1.x)
print(p1.a)