import sys
var1 = sys.argv[1]
var2 = sys.argv[2]
with open(var1) as f1:
    l = []
    xk = ''
    yk = ''
    r = ''
    for i in f1:
        l.append(i.strip(""))
        xk, yk = l[0].strip().split(" ")
    r = l[1]
xk = float(xk)
yk = float(yk)
r = float(r)

with open(var2) as f2:
    l = []
    for i in f2:
        x = ''
        y = ''
        l.append(i.strip(""))
    for n, j in enumerate(l):
        x,y=l[n].strip().split(" ")
        x=float(x)
        y=float(y)
        total=int((x - xk) ** 2 / r ** 2 + (y - yk) ** 2 / r ** 2)
        if int((x - xk) ** 2 / r ** 2 + (y - yk) ** 2 / r ** 2) == 0:
            print(f'{total} - точка лежит на окружности')
        elif int((x - xk) ** 2 / r ** 2 + (y - yk) ** 2 / r ** 2) == 1:
            print(f'{total} - точка внутри')
        else:
            print(f'{total} - точка снаружи')










































