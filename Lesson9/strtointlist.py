strList = ["54" , "32" , "421"]
def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])
    return strList
def test(strList):
    strList = toNumbers(strList)
    print(strList)
test(strList)
input()
