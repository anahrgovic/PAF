import matplotlib.pyplot as plt
from math import sin, cos

def xy_putanja(v0,theta,t):
    vx=v0*cos(theta)
    vy=v0*sin(theta)
    
    x=0
    y=0
    dt=0.5
    g=9.81
    N=t*2
    pomak_x=[]
    pomak_y=[]
    vrijeme=[]
    for i in range(N):
        x=x + vx*dt
        vy=vy - g*t
        y=y + vy*dt
        t += dt
        pomak_x.append(x)
        pomak_y.append(y)
        vrijeme.append(t)

    while True:
        if y==1:
            break
    

    plt.plot(pomak_x,pomak_y)
    plt.title('x-y graf')
    plt.show() 


        