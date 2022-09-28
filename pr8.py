import math
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

def mediana():
    global a
    global b
    global c
    if a<b+c and b<a+c and c<a+b:
        mediana = 0.5 * math.sqrt(2*b**2+2*c**2-a**2)
        return mediana
    else:
        print("Nu e triunghi")     
print(mediana())