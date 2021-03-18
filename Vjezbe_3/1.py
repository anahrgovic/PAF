import math
class Particl:
    def __init__(self, mass, x_0):
        self.mass = mass
        self.x_0 = x_0

    def printInfo(self):
        print('Čestica ima masu {0:.2f} i u početnom trenutku nalazi se u položaju x={1:.2f}'.format(self.mass,self.x_0))

    def udaljenost(self):
        d=math.fabs(self.x_0)
        print('Udaljenost od ishodišta je {0:.2f}'.format(d))
    
    def udaljenost_tocke(self,X):
        self.X=X
        x=math.fabs(self.X - self.x_0)
        print('Udaljenost točke je {0:.2f}'.format(self.X, self.x_0))

p1=Particl(10,-5)
p1.printInfo()

p1.mass=20
p1.printInfo()

p1.udaljenost()
p1.udaljenost_tocke(12)
