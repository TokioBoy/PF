def addInterest(balance,rate):
    return balance*rate
def test():
    balance = float(input("Enter your balance:  "))
    balance = addInterest(balance, float(input("Enter a rate:  ")))
    print(balance)
test()
#GOOD WAY TO DO
