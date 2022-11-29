def main():
    a = 1
    b = 1
    f = 0
    print(a , b)
    while f < 10:
        result1 = a + b
        result2 = result1 + b
        a = result1
        b = result2
        print(result1 , result2)
        f = f + 1
main()
        
