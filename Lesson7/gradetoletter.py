def main():
    numgrade = (int(input("Enter number:  ")))
    if (numgrade == 5):
        print("A")
    elif(numgrade == 4):
        print("B")
    elif(numgrade == 3):
        print("C")
    elif(numgrade == 2):
        print("D")
    elif(numgrade == 1):
        print("F")
    elif(numgrade == 0):
        print("F")
main()

def main2():
    grade_num = int(input("Please enter a number:  "))
    print("FFDCBA"[grade_num])
main2()
