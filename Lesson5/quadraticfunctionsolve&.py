from math import sqrt
a = float(input("Enter the value of a:  "))
b = float(input("Enter the value of b:  "))
c = float(input("Enter the value of c:  "))

def quadratic():
    x1 = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)
    return x1,x2
first,second = quadratic()
print("x1 = ",first)
print("x2 = ",second)

input()
