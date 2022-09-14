n = int(input("n="))
def factorial(x):
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    return fact
print(factorial(n))