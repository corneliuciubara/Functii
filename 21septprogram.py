import math
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

#cel mai mare divizor comun
def dc(x, y, z):
    if (y==0):
        return abs(x)
    else:
        return dc(y, x%y, z)

print("Cel mai mare divizor comun:", dc(a, b, c))

#cel mai mic multiplu comun
def lcm(x, y, z):
    lst1=[]
    lst2=[]
    lst3=[]
    lst4=[]
    lst1=(list(range(x,15*x,x)))
    lst2=(list(range(y,15*z,y)))
    lst3=(list(range(z,15*z,z)))
    for i in lst1:
        for x in lst2:
            for z in lst3:
                if i == x == z:
                    lst4.append(i)
    return min(lst4)
print("Cel mai mic multiplu comun:", lcm(a, b, c))

#numarul maxim
def max(x, y, z):
    lst = []
    if x>y and x>z:
        lst.append(x)
    if y>x and y>z:
        lst.append(y)
    if z>x and z>y:
        lst.append(z)
    return lst
print("Numarul maxim:", max(a, b, c))

#numarul minim
def min(x, y, z):
    lst = []
    if x<y and x<z:
        lst.append(x)
    if y<x and y<z:
        lst.append(y)
    if z<x and z<y:
        lst.append(z)
    return lst
print("Numarul minim:", min(a, b, c))

#toti divizorii comuni
def commDiv(x, y, z):
    res = []
    for i in range(2, int(min(x, y, z) / 2 + 1), 2):
        if (x % i == 0) and (y % i==0) and (z % i == 0):
            res.append(i)
    return res

print("Toti divizorii comuni:", commDiv(a, b, c))

def tdc(x,y,z):
    res = []
    for i in range(2, int(min(x,y,z)/2+1), 2):
        if (x%i==0) and (y%i==0) and (z%i==0):
            res.append(i)
    return res
print(tdc(a,b,c))
