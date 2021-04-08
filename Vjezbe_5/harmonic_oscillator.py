import math
import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self,k,m,x0,v0):
        self.k=k
        self.m=m
        self.x=x0
        self.v=v0
        self.a=-(self.k*self.x)/self.m
        self.t=0
        self.x_lista=[]
        self.v_lista=[]
        self.a_lista=[]
        self.t_lista=[]

    def oscillate(self,dt,t):
        N=int(t/dt)
        for i in range(N):
            self.a=-(self.k*self.x)/self.m
            self.v=self.v + self.a*dt
            self.x=self.x + self.v*dt
            self.t +=dt
            self.x_lista.append(self.x)
            self.v_lista.append(self.v)
            self.a_lista.append(self.a)
            self.t_lista.append(self.t)
        return (self.x_lista,self.v_lista,self.a_lista,self.t_lista)

    def plot_trajectory(self,dt,t):
        self.oscillate(dt,t)
        plt.subplot(131)
        plt.plot(self.t_lista,self.x_lista)
        plt.title('x-t graf')
        plt.subplot(132)
        plt.plot(self.t_lista,self.v_lista)
        plt.title('v-t graf')
        plt.subplot(133)
        plt.plot(self.t_lista,self.a_lista)
        plt.title('a-t graf')
        plt.show()
        
        
        





h1=HarmonicOscillator(10,0.1,0.3,0)
#h1.oscillate(0.01,2)
h1.plot_trajectory(0.01,2)