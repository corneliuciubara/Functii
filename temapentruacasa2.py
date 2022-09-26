import math
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

#cel mai mare divizor comun
def cmdc(x, y, z):
    for i in range(min(x, y, z), 0):
        if ((i%x==0) and (i%y==0) and (i%z==0)):
            return i
print("Cel mai mare divizor comun", cmdc(a, b, c))

#cel mai mic multiplu comun
def lcm(x, y, z):
    for i in range(max(x,y,z), x*y*z+1, 1):
        if (i%x==0) and (i%y==0) and (i%z==0):
            return i
print("Cel mai mic multiplu comun:", lcm(a, b, c))

#numarul maxim
def max(x, y, z):
    if x>y:
        if z>x:
            return z
        else:
            return x
    else:
        if z>y:
            return z
        else:
            return y
print("Numarul maxim:", max(a, b, c))

#numarul minim
def min(x, y, z):
    if x>y:
        if y>z:
            return z
        else:
            return y
    else:
        if z>x:
            return x
        else:
            return z
print("Numarul minim:", min(a, b, c))

#toti divizorii comuni
def tdc(x, y, z):
    lst = []
    for i in range(1, int(min(x, y, z) + 1), 1):
        if (x % i == 0) and (y % i==0) and (z % i == 0):
            lst.append(i)
    return lst
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
print("Cei mai mici 3 multipli comuni", cmmmc(a, b,c))

tmp = 0
for i in range(3):
    tmp = cmmmc(a,b,c,tmp+1)
    print("Multiplul", i, ":", tmp)

#triunghi
def ft(x, y ,z):
    p = (x+y+z)/2
    if ((x+y>z) and (x+z>y) and (y+z>x)):
        aria = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return x+y+z, aria
    else: 
        return "Nu e triunghi"
print(ft(a,b,c))

#ax2+bx+x
def sec(x,y,z):
    str1 = "Prima solutie este"
    str2 = "A doua solutie este"
    str3 = "  Si  "
    d = y**2 - 4*x*z
    if d>0:
        s1 = (-y-(math.sqrt(d)))/(2*x)
        s2 = (-y+(math.sqrt(d)))/(2*x)
        strs = str(str1) + str(s1) + str(str3) + str(str2) + str(s2)
    if d<0:
        return "Delta este negativ"
    if d == 0:
        s1 = s2 = -y/2*x
    return strs
print(sec(a,b,c))
