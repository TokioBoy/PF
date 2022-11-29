def main(lst):
    largest = [0,""]
    for i in lst:
        if largest[0] < (i[1]*i[2])/2:
            largest[0] = (i[1]*i[2])/2
            largest[1] = i[0]
    print(largest[1])
    return largest[1]
    #for function that checking conditions
rectangles = [('red',43545,5325),('green',423244,3254),('blue',5434445,324)]
#creates a list
main(rectangles)
