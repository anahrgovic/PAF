import math
class Particl:
    def __init__(self, mass, x_0):
        self.mass = mass
        self.x_0 = x_0

    def printInfo(self):
        print('Čestica ima masu {0:.2f} i u početnom trenutku nalazi se u položaju x={1:.2f}'.format(self.mass,self.x_0))

    