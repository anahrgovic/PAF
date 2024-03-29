import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

class particle:
    def __init__(self,E,B,v,m,q,dt=0.01):
        self.E=E
        self.B=B
        self.v=v
        self.m=m
        self.q=q
        self.dt=dt
        self.r=np.array((0,0,0))
        self.r_x= []
        self.r_y = []
        self.r_z = []
        self.r_x.append(self.r[0])
        self.r_y.append(self.r[1])
        self.r_z.append(self.r[2])
        self.t=0


    def reset(self):
        del self.E
        del self.B
        del self.v
        del self.m
        del self.q
        del self.dt
        del self.r
        del self.r_x
        del self.r_y
        del self.r_z
        del self.t

    def a(self, v):
        return((self.q/self.m)*(self.E+ np.cross(v,self.B)))
        

    def move(self):
        #a = (self.q/self.m)*(self.E+ np.cross(self.v,self.B))
        self.v = self.v + self.a(self.v)*self.dt
        self.r = (self.r + self.v*self.dt)
        self.r_x.append(self.r[0])
        self.r_y.append(self.r[1])
        self.r_z.append(self.r[2])
        self.t += self.dt
        #print(a,self.v,self.r_x, self.r_y,self.r_z)

    def euler(self,t):
        while self.t <= t:
            self.move()
        return self.r_x, self.r_y,self.r_z

    def __move_RK(self):
        self.t += self.dt
        k1v = self.a(self.v)*self.dt
        k1r = self.v * self.dt
        k2v = (self.a(self.v + k1v/2)*self.dt)
        k2r = (self.v + (k1v/2)) * self.dt
        k3v = (self.a(self.v+k2v/2)*self.dt)
        k3r = (self.v+k2v/2) * self.dt
        k4v = (self.a(self.v+k3v/2)*self.dt)
        k4r = (self.v+k3v) * self.dt

        self.v=self.v + (k1v + 2*k2v + 2*k3v + k4v)/6
 
        self.r=self.r + (k1r + 2*k2r + 2*k3r + k4r)/6
        self.r_x.append(self.r[0])
        self.r_y.append(self.r[1])

        self.r_z.append(self.r[2])

    def evolve_RK(self,t):
        while self.t <=t:
            self.__move_RK()
        return self.r_x,self.r_y,self.r_z

    def plot_trajectory(self):
        ax = plt.axes(projection = "3d")
        ax.plot3D(self.r_x,self.r_y,self.r_z)
        plt.show()     

p1=particle(np.array((0,0,0)),np.array((0,0,1)),np.array((0.1,0.1,0.1)),1,1)
#p1.move()
#p1.euler(20)
#p1.plot_trajectory()
#p1.a()
#p1.evolve_RK(1)

