x1 = int(input("Enter a value x1:  "))
x2 = int(input("Enter a value x2:  "))
x3 = int(input("Enter a value x3:  "))
try:
    if(x1>x2>x3):
        print("The biggest num is:" ,x1)
    elif(x2>x1>x3):
        print("The biggest num is:" ,x2)
    else:
        print("The biggest num is:" ,x3)
except:
    print("Something wrong")
    
