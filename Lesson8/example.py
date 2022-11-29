def f1():
    x = 20
    def f2():
        x = 3
        print(x)
    f2()
f1()
