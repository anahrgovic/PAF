import math
import numpy as np

class Pendulum:
    def __init__(self, mjerna_jedinica, theta, l, m, dt):
        self.theta = theta
        self.theta0 = theta
        self.l = l
        self.m = m
        self.dt = dt
        self.t = 0
        self.omega = 0
        self.k = 0
        self.__kut()
        self.thetal = []
        self.thetal.append(self.theta)
        self.tl = []
        self.tl.append(self.t)
        print(self.theta, self.l, self.m)

    def __kut(self):
        if self.theta > 10:
            print("Radi se o velimom kutu:")
        else:
            print("Radi se o malom kutu.")

    def change_theta(self, mjerna_jedinica, theta):
        self.theta = theta
        if mjerna_jedinica == "rad":
            print("Nova kut je" ,self.theta, "radijana")
        elif mjerna_jedinica == "deg":
            print("Nova kut je" ,self.theta, "stupnjeva")
            self.theta = self.theta*math.pi/180
        self.__kut()
        if self.theta < self.theta0:
            print("novi je manji")
        else:
            print("novi je veci")

    def __oscillate(self):
        self.alpha = -9.81 * math.sin(self.theta)
        self.omega = self.omega + self.alpha * self.dt
        self.theta = self.theta + self.omega * self.dt
        self.t = self.t + self.dt

        self.thetal.append(self.theta)
        self.tl.append(self.t)

    def oscillate(self, t):
        while self.t <= t:
            self.__oscillate()

        return self.thetal, self.tl

    def oscillate_ar(self, k, t):
        while self.t <= t:
            self.alpha = ((self.k * self.omega) / self.m -9.81) * math.sin(self.theta)
            self.omega = self.omega + self.alpha * self.dt
            self.theta = self.theta + self.omega * self.dt
            self.t = self.t + self.dt
        
            self.thetal.append(self.theta)
            self.tl.append(self.t)

        return self.thetal, self.tl

    def stopping(self, t):
        for i in self.t:
            if self.omega < 0:
                print("Zaustavilo se")
            else:
                break

                #ovo ne radi hahaha ovo zadnje zaustavljanje!!!