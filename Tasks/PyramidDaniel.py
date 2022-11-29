number = int(input("Enter your number:  "))
def pira(n):
    n=n+1
    for y in range(n,0,-1):
        print(" "*(y-1)+"# "*(n-y))

pira(number)
def stebel():
    s = int(number/2)
    dlinna = int(number/2.5)
    shirina = int(number/2)
    while(shirina>0):
        print(s*" " , "# " *dlinna)
        shirina = shirina - 1
stebel()
