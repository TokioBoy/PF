def name(stri):
    lst = []
    first = []
    last = []
    lst = stri.split()
    first = lst[1][0].upper() + lst[1][1:-1] + lst[1][-1].upper()
    last = lst[0][0].upper() +lst[0][1:-1] + lst[0][-1].upper()
    print(first + " " + last)

name("vladyslav zolotarevksyi")
