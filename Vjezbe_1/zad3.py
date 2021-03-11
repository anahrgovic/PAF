x1 = float(input('Unesi x koordinatu prve točke:'))
x2 = float(input('Unesi x koordinatu druge točke:'))
y1 = float(input('Unesi y koordinatu prve točke:'))
y2 = float(input('Unesi y koordinatu druge točke:'))
k = (y2-y1)/(x2-x1)
l = -k*x1 + y1
if l<0:
    print(f'y = {k}x {l}')
elif l==1:
    print(f'y = {k}x')
else:
        print(f'y = {k}x + {l}')
