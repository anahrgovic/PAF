import math
import numpy as np

class Planet:
    def __init__(self, name,  m, r, v):
        self.name = name
        self.m    = m
        self.r    = r 
        self.v    = v 
        self.a    = np.array((0.,0.)) 

       
        self.dr = []

        
        self.x = []
        self.y = []

        self.x.append(r[0])
        self.y.append(r[1])

class Universe:
    
    G = 6.67408e-11
    day = 60*60*24

    def __init__(self, dt=0.1):
        self.planets = [] 
        self.dt = dt * self.day 
        self.t = [] 

    def add_planet(self, planet):
        self.planets.append(planet)

    def evolve(self, time, method = 'euler'):
        self.t.append(0)
        steps = int(time/self.dt) 
        i=1
        while i < steps:
            self.__move(i) 
            i += 1

    def __move(self, i):
        self.t.append(self.t[i-1] + self.dt) 

        for p1 in self.planets: 
            p1.dr.clear() 
            for p2 in self.planets: 
                if (p1 == p2):
                    p1.dr.append(np.array((0.,0.)))
                else: 
                    p1.dr.append((-1*self.G*p2.m*(p1.r - p2.r))/(np.linalg.norm(p1.r - p2.r))**3)

            
            p1.a *= 0 
            for dr in p1.dr:
                p1.a += dr

            
            p1.v += p1.a*self.dt
            p1.r += p1.v*self.dt

            p1.x.append(p1.r[0])
            p1.y.append(p1.r[1])
