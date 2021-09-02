import matplotlib.pyplot as plt
import math
import numpy as np

class Pendulum:
    def __init__(self,theta,l,m):
        self.l=l
        self.m=m
        self.theta=theta
        self.__kut(self.theta)
        self.l_=[]
        

        
    def __kut(self,theta):
            if theta<=10:
                print('Unesen je mali kut otklona.')

    def change_theta(self,RiliS,n_theta):
        self.RiliS=RiliS
        self.theta+=n_theta
        if self.RiliS==0:
            self.theta=np.radians(self.theta)
            n_theta=np.radians(n_theta)
            print(self.theta) 
        elif self.RiliS==1:
            print(self.theta)

    def reset(self):
        del self.theta
        del self.l
        del self.m
        del self.l_
    
    def __oscillate(self,dt,t):
        self.t=t
        self.dt=dt
        self.k=1
        self.v=0
        self.v_=[]
        self.a_=[]
        self.t_=[]
        N=int(t/dt)
        for i in range(N):
            self.a=-(self.k*self.l)/self.m
            self.v=self.v + self.a*dt
            self.l=self.l + self.v*dt
            self.t +=dt
            self.l_.append(self.l)
            self.v_.append(self.v)
            self.a_.append(self.a)
            self.t_.append(self.t)
        #print(self.a,self.v,self.l,self.t)
        #print(self.l_,self.t_)
        return (self.l_,self.v_,self.a_,self.t_)
        


    def evolve(self,dt,t):
        self.__oscillate(dt,t)
        return self.l_,self.t_,self.v_,self.a_
        #print(self.l_,self.t_)
        #print(f"length of time: {len(self.t_)} ")
        #print(f"length of position: {len(self.l_)}" )
        #return self.l_,self.t_

    #def plot_trajectory(self):
        #self.evolve(self.dt,self.t)
        #plt.plot(self.t_,self.l_)
        #plt.title('l-t graf')
        #plt.show()

    def __move_with_ar(self,dt,t):
        g=9.81
        k=1
        self.t=t
        self.dt=dt
        self.v=0
        self.v_=[]
        self.a_=[]
        self.t_=[]
        N=int(t/dt)
        for i in range(N):
            self.a = -g + (k*self.v)
            self.v=self.v + self.a*dt
            self.l=self.l + self.v*dt
            self.t +=dt
            self.a_.append(self.a)
            self.l_.append(self.l)
            self.v_.append(self.v)
            self.t_.append(self.t)
            #print(self.a_)
            #print(self.l_)
            #print(self.v_)
            #print(self.t_)
            
       

    def run_event_with_ar(self,dt,t):
        self.__move_with_ar(dt,t)
        return self.l_,self.t_,self.v_