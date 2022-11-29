def Sumlist(list):
    sum = 0
    for i in range(len(list)):
        sum+=list[i]
    return sum


def test(list):
    print(Sumlist(list))


list = [2, 4, 8, 16, 32, 64]
test(list)
input()
