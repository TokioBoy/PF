def main():
    rectangles = [('red',435,325),('green',4244,3254),('blue',54335,324)]
    if((rectangles[0][1]*rectangles[0][2])>
       (rectangles[1][1]*rectangles[1][2])):
        print(rectangles[0][0])
    elif((rectangles[1][1]*rectangles[1][2])>
       (rectangles[2][1]*rectangles[2][2])):
        print(rectangles[1][0])
    else:
        print(rectangles[2][0])
main()
