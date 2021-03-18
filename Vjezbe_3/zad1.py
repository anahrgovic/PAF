import matplotlib as plt

import math
class Particle:
    def __init__(self,v0,theta,x0):
        self.v0=v0
        self.theta=theta
        self.x0=x0
    def printInfo(self):
        print('Čestica je iz početnog položaja {0:.2f} m izbačena početnom brzinom {1:.2f} m/s pod kutom od {2:.2f} stupnjeva.'.format(self.x0,self.v0,self.theta))
    def reset(self):
        self.v0=0
        self.theta=0
        self.x0=0
    def __move(self, t):
        self.t=t
        


p1=Particle(10,45,3)
p1.printInfo()
p1.reset()
print(p1.v0,p1.theta,p1.x0)
p1.move(10)
print(p1.t)
