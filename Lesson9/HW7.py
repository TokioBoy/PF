def ToNumbers(list):
    for i in range(len(list)):
       list[i]=int(list[i])
    return list

def test(list):
    list = ToNumbers(list)
    print(list)

list = ["2", "4", "8", "16", "32", "64"]
test(list)
input()
