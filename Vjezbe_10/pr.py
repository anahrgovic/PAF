E=np.array((0,0,0))
B=np.array((0,0,1))
v=np.array((0.1,0.1,0.1))
q=1
m=1
x=q/m
vp=np.cross(v,B)
c = np.dot(x,E)
#print(c)
#print(vp)
#print(a[0])
a = x*(E+ np.cross(v,B))
v = a*1
print(v)
print(a)
x = 
plt.plot(self.r_[0],self.r_[1],self.r_[2])
plt.show() 