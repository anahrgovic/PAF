import bullet as blt

b1=blt.Bullet(100,2,0.01,0)
b1.evolve(2)
b1.range()
plt.subplot(311)
plt.plot(b1.x_,b1.y_)
plt.subplot(312)
plt.plot(b1.x_,b1.t_)
plt.subplot(313)
plt.plot(b1.y_,b1.t_)
plt.show() 