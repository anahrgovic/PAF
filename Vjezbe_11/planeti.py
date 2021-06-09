import numpy as np
import math
class Gravity:
    def __init__(self,ms,mz,G,xs,ys,xz,yz,vxs,vys,vxz,vyz,dt):
        self.ms = ms
        self.mz = mz
        self.G = G
        self.rs = np.array([xs,ys])
        self.rz = np.array([xz,yz])
        self.vs = np.array([vxs,vys])
        self.vz = np.array([vxz,vyz])
        self.dt = dt
        self.t = 0
        #self.az = 0
        #self.asn = 0
        self.xs_ = []
        self.ys_ = []
        self.xz_ = []
        self.yz_ = []
    def akc_s(self,rs,rz):
        d = (rs-rz)**2
        n = math.sqrt(d[0]+d[1])
        return (-self.G*self.mz*(rs-rz))/n**3
    def akc_z(self,rs,rz):
        d = (rz-rs)**2
        n = math.sqrt(d[0]+d[1])
        return (-self.G*self.ms*(rz-rs))/n**3
    def Euler(self,t):
        while self.t <= t:
            self.asn = self.akc_s(self.rs,self.rz)
            self.vs = self.vs + self.asn*self.dt
            self.rs = self.rs + self.vs*self.dt
            
            self.az = self.akc_z(self.rs,self.rz)
            self.vz = self.vz + self.az*self.dt
            self.rz = self.rz + self.vz*self.dt
            
            self.t+= self.dt
            self.xs_.append(self.rs[0])
            self.ys_.append(self.rs[1])
            self.xz_.append(self.rz[0])
            self.yz_.append(self.rz[1])
            
        return self.xs_,self.ys_,self.xz_,self.yz_