from re import A

a = float(input("a="))
b = float(input("b="))
a1 = float(input("a1="))
a2 = float(input("a2="))
a3 = float(input("a3="))
a4 = float(input("a4="))
a5 = float(input("a5="))
a6 = float(input("a6="))
a7 = float(input("a7="))
a8 = float(input("a8="))
a9 = float(input("a9="))
a10 = float(input("a10="))
m = float(input("m="))
n = float(input("n="))

def maxim():
    global a
    global b
    if a>b:
        return a
    if b>a:
        return b
def minim():
    global a
    global b
    if a<b:
        return a
    if b<a:
        return b

print(maxim())
print(minim())

def e1(s):
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7
    global a8
    s = max(min(a1,a2), max(a3,a4)) + min(max(a5,a6),min(a7,a8))
    return s
print("a)",e1(m))

def e2(s):
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7
    global a8
    global a9
    global a10
    s = min(a1,a2) + min(a3,a4) + min(a5,a6) + min(a7,a8) + min(a9,a10) + max(a1,a2) + max(a3,a4) + max(a5,a6) + max(a7,a8) + max(a9,a10)
    return s
print("b)",e2(n))
