n1 = (input("n1="))
n2 = (input("n2="))
b = int(input("b="))

print("n1 =", n1)
print("n2 =", n2)
print("b =", b)

def tostr(num, base):
    result = ""
    while num > 0:
        dig =  num % base
        num = num // base
        result = str(dig)+result
    return result

def fromstr(str, base):
    result = 0
    for i in range(0, len(str)):
        ch = str[i]
        dig = int(ch) - int('0')
        if dig >= base:
            print("Error")
            return -1
        result = result*base + dig
    return result

print("Numerele in baza 10:", fromstr(n1, b), fromstr(n2,b))
#print("From String:", fromstr(str(n1), n2))

def suma(num1, num2, base):
    sum = fromstr(num1,base) + fromstr(num2,base)
    return tostr(sum,base)
print("Suma:", suma(n1, n2, b))

def difference(num1, num2, base):
    diff = fromstr(num1,base) - fromstr(num2,base)
    return tostr(diff,base)
print("Diferenta:", difference(n1, n2, b))

def inmultirea(num1, num2, base):
    produs = fromstr(num1,base) * fromstr(num2,base)
    return tostr(produs,base)
print("Inmultirea:", inmultirea(n1, n2, b))