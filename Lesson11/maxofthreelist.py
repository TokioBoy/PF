x1 = int(input("Enter a value x1:  "))
x2 = int(input("Enter a value x2:  "))
x3 = int(input("Enter a value x3:  "))
list = [x1 , x2 , x3 ]
max_num = x1
for i in range (len(list)):
    if(max_num < x2):
        max_num = x2
    if(max_num < x3):
        max_num = x3
print(max_num)
    
