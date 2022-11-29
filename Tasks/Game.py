import random

result = 0
while(result < 1):
    answer = "no"
    yours = int(input("Whats hidden number?"))
    hidden = [random.randint(0,100)]
    for i in hidden:
        hidden = i
    if yours == hidden:
        print("You won!")
        answer = input("Do you wanna play again?(type'no' if you dont want)")
        if answer == "no":
            result = result + 1
        
        
