def jedzb_pravca (x1,x2,y1,y2):
    k = (y2-y1)/(x2-x1)
    l = -k*x1 + y1
    if l<0:
        print(f'y = {k}x {l}')
    elif l==1:
        print(f'y = {k}x')
    else:
        print(f'y = {k}x + {l}')

pravac = jedzb_pravca (2,3,4,5)