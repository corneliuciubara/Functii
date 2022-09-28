import math
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
d = int(input('d='))

def pa(x ,y, z):
    p = x + y + z
    sp = p/2
    A = math.sqrt(sp*(sp-x)*(sp-y)*(sp-z))
    return print("Perimetru=",p,"Aria=",A)
if ((a > 0) and (b > 0) and (c > 0) and (d > 0)):
    if ((a+b>c) and (b+c>a) and (a+c>b)):
        print("Triunghiul ABC:")
        pa(a,b,c)
    else:
        print("ABC nu e triunghi")
    if ((a+b>d) and (b+d>a) and (a+d>b)):
        print("Triunghiul ABD:")
        pa(a,b,d)
    else:
        print("ABD nu e triunghi")
    if ((c+b>d) and (b+d>c) and (c+d>b)):
        print("Triunghiul BCD:")
        pa(b,c,d)
    else:
        print("BCD nu e triunghi")
    if ((c+a>d) and (a+d>c) and (c+d>a)):
        print("Triunghiul ACD:")
        pa(a,c,d)
    else:
        print("ACD nu e triunghi")
else:
    print("Nu sunt numere naturale")