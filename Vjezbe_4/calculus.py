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


    
