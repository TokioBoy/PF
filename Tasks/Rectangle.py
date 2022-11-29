def main():
    a = int(input("Enter the weight of the rectangle:  "))
    b = int(input("Enter the width of the rectangle:  "))
    d = a * b
    c = "#"

    print (a * b * c)
    while d > 0:
        print((1*c) + (((a*b)-2)*" ") + (1*c))
        d = d - 1
    if (d == 0):
        print(a * b * c)
main()
