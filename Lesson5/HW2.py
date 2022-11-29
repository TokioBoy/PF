def print_rectangle(m ,n):
    for i in range(m):
        for j in range(n):
            print('V', end='')
        print()
 
m = int(input("Enter height:  "))
n = int(input("Enter weight:  "))
print_rectangle(m , n)
input()
