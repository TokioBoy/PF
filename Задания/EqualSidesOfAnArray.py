array = [1,100,50,-51,1,1]
def main():
    for i in array:
        if sum(array[:array.index(i)]) == sum(array[array.index(i)+1:]):
            print(array.index(i))
        else:    
            print(-1)
main()

