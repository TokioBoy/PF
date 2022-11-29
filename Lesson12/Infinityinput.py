def main():
    a = 0
    result = 0
    while (a == 0):
        nums = str(input("Enter your numbers:  "))
        if (nums == "stop"):
            a = a + 1
            print(result)
        else:
            result = int(nums) + result
main()

    
