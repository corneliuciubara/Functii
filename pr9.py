import math
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

def inaltimea():
    global a
    global b
    global c
    if a<b+c and b<a+c and c<a+b:
        sp = (a+b+c)/2
        aria = math.sqrt(sp*(sp-a)*(sp-b)*(sp-c))
        h=(2*aria)/(a)
        return print("Inaltimea triunghiului ABC:", h )
    else:
        print("Nu e triunghi")    
print(inaltimea())