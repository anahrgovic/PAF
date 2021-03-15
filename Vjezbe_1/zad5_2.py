import matplotlib.pyplot as plt

def odredi_pravac(x1,x2,y1,y2, znak):
    plt.xlabel('x')
    plt.ylabel('y')
    x_koordinate=[x1,x2]
    y_koordinate=[y1,y2]
    plt.plot(x_koordinate, y_koordinate)
    if znak==1:
        naziv_slike=input('Unesi naziv slike:')
        plt.savefig (f'{naziv_slike}.pdf')
    elif znak==0:
        plt.show()

odredi_pravac(5,10,2,8,0)