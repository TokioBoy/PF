def rect_with_hole(rows,cols,symb):
    lst=[]
    belly = []
    lst.append(f"{symb}"*rows)
    lst.append(" "*rows)
    belly = symb+lst[1][1:-1]+symb
   
    for row in range(1,2):
        #print("# "*cols)
        for col in range(1,cols+1):
            if col == row or col == cols:
                print(lst[0])
            else:
                print(belly)
        
rect_with_hole(8, 3,"#")
