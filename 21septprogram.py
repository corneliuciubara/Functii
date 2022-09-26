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
def tdc(x, y, z):
    res = []
    for i in range(2, int(min(x, y, z) / 2 + 1), 2):
        if (x % i == 0) and (y % i==0) and (z % i == 0):
            res.append(i)
    return res

print("Toti divizorii comuni:", tdc(a, b, c))

#cei mai mici 3 multipli comuni
def cmmmc(x, y, z, mare=0):
    if mare==0:
        mare = max(x,y,z)
    lcm = x*y*z
    while True:
        if ((mare % x == 0) and (mare % y == 0) and (mare % z == 0)):
            lcm = mare
            break
        mare += 1
    return lcm
print("Cinci multipli comuni", cmmmc(a, b,c))

tmp = 0
for i in range(3):
    tmp = cmmmc(a,b,c,tmp+1)
    print("Multiplul", i, ":", tmp)

#triunghi
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
def ft(x, y ,z):
    if ((x+y>z) and (x+z>y) and (y+z>x)):
        return x+y+z
    else: 
        return "Nu e triunghi"
print(ft(a,b,c))

#ax2+bx+x
def sec(x,y,z):
    str1 = "Prima solutie este"
    str2 = "A doua solutie este"
    str3 = "  Si  "
    lst = []
    d = y**2 - 4*x*z
    if d>0:
        s1 = (-y-(math.sqrt(d)))/(2*x)
        s2 = (-y+(math.sqrt(d)))/(2*x)
        strs = str(str1) + str(s1) + str(str3) + str(str2) + str(s2)
    if d<0:
        return "Delta este negativ"
    if d == 0:
        s1 = s2 = -y/2*x
    lst.append(strs)
    return lst
print(sec(a,b,c))
