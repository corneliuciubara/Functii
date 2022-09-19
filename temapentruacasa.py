import math

a = int(input("a="))
b = int(input("b="))

#suma
def suma(x, y):
    return x+y
print("Suma numerelor:", suma(a, b))

#produsul
def produs(x, y):
    return x*y
print("Produsul numerelor:", produs(a, b))

#media aritmetica
def mediaart(x, y):
    return (x+y)/2
print("Media aritmetica a numerelor:", mediaart(a, b))

#cel mai mare divizor comun
def dc(x, y):
    if (y==0):
        return abs(x)
    else:
        return dc(y, x%y)
print("Cel mai mare divizor comun:", dc(a, b))


#cel mai mic mutiplu comun
def lcm(x, y):
   if x > y:
       mare = x
   else:
       mare = y

   while(True):
       if ((mare % x == 0) and (mare % y == 0)):
           lcm = mare
           break
       mare += 1

   return lcm
print("Cel mai mic multiplu comun:", lcm(a, b))

#numarul minim
def nrmin(x, y):
    z = min(x, y)
    return z
print("Numarul minim:", nrmin(a, b))

#numarul maxim
def nrmax(n, m):
    q = max(n, m)
    return q
print("Numarul maxim:", nrmax(a, b))

#suma numerelor in formatul a+b=c
def sum(x, y):
    c = a + b
    return c
print("Suma numerelor in formatul", a, "+",b, "=", sum(a, b))

#produsul numerelor in formatul a*b=c
def produs(x, y):
    c = a * b
    return c
print("Produsul numerelor in formatul", a, "*",b, "=", produs(a, b))

#toti divizorii comuni
import math
def commDiv(a,b):
    res = []
    for i in range(2, int(min(a,b) / 2 + 1), 2):
        if (a % i == 0) and (b % i==0):
            res.append(i)
    return res

print("Toti divizorii comuni:", commDiv(a, b))

#cinci multipli comuni
def cmmmc(x, y, mare=0):
    if mare==0:
        mare=max(x,y)
    lcm=x*y
    while(True):
        if ((mare % x == 0) and (mare % y == 0)):
            lcm = mare
            break
        mare += 1
    return lcm
print("Cinci multipli comuni:", cmmmc(a, b))

tmp=0
for i in range(5):
    tmp = cmmmc(a,b,tmp+1)
    print("Multiplul",i,":",tmp)


#cifrele care se contin in ambele numere
def ccan(x, y):
    setX = set(t for t in str(x))
    setY = set(t for t in str(y))
    return sorted(setX.intersection(setY))
    
print ("Cifrele care se contin in ambele numere:", ccan(a, b))

#cifrele care se contin in primul numar si nu sunt in al doilea
def ccpnd(x, y):
    setX = set(t for t in str(x))
    setY = set(t for t in str(y))
    return sorted(setX.difference(setY))

print ("Cifrele care se contin in primul numar si nu sunt in al doilea", ccpnd(a, b))

#prietene

def divizori(a):
    res = []
    for i in range(2, int(a / 2 + 1), 2):
        if (a % i == 0):
            res.append(i)
    return res

def nnnn(a,b):
    divizoriA = divizori(a)
    divizoriB = divizori(b)

    if len(divizoriA) == len(divizoriB):
        print("numerele :",a,",",b,"sunt PRIETENE")
    else:
        print("numerele :",a,",",b,"NU sunt PRIETENE")


nnnn(a,b)