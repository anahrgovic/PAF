import Pendulum as pnd

p1=pnd.Pendulum(5,3,2,0)
p2=pnd.Pendulum(3,2,5,0)

p1.change_theta("rad",10)
p2.change_theta("deg",20)