def addInterest(balance,rate):
    return balance*rate
def test():
    balanceList = [1500 , 2134 , 5467 , 9874]
    rate = float(input("Enter a rate:  "))
    for balance in balanceList:
        balance = addInterest(balance,rate)
        print(balance)     
test()
