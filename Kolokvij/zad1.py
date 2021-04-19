import matplotlib.pyplot as plt
import math
import numpy as np

class Vertikalnihitac:
    def __init__(self,v0,h0):
        self.v0=v0
        self.h0=h0

    def printInfo(self):
         print('Objekt je uspješno stvoren. Početna brzina objekta je {0:.2f} m/s, početna visina je {1:.2f} m.'.format(self.v0,self.h0))


vh1=Vertikalnihitac(10,5)
vh1.printInfo()