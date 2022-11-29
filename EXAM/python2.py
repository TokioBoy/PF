def main():
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))
    #creates two variables
    lst = []
    #creates a empty list
    for i in range(first_num, second_num):
        if i % 7 == 0 and i % 5 != 0:
            lst.append(str(i))
            #adding element to list if they pass "if" condition
    print(",".join(lst))
    #print a list
main()