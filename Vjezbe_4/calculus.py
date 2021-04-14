import numpy as np

def deriv(func,x,h):
    d=(func(x+h)-func(x-h))/(2*h)
    return d

def derivacija(func,x1,x2,h):
    lista=[]
    xlista=np.arange(x1,x2,h)
    for x in xlista:
        d=(func(x+h)-func(x-h))/(2*h)
        lista.append(d)
    return xlista,lista

def integr(func,a,b,N):
    dx=(b-a)/N
    gornja=0
    donja=0
    x_gornja=a
    x_donja=a+dx
    for i in range(N):
        #print(x_donja,x_gornja)
        gornja +=func(x_gornja)*dx
        donja +=func(x_donja)*dx
        #print(gornja,donja)
        x_gornja +=dx
        x_donja +=dx
        
    return gornja, donja

def integr_tr(func,a,b,N):
    dx=(b-a)/N
    x=a
    suma=0
    for i in range(N):
        suma += (func(x)+func(x+dx))
        x +=dx
        integral= (dx/2)*suma
    return integral
  

    
