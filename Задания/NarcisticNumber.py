def main():
    print("This program determines if a number is Narcistic.")
    print()
    number = int(input("Enter a number: "))
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if number == sum:
        print(number, "is a Narcistic number.")
    else:
        print(number, "is not a Narcistic number.")
main()