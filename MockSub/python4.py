def main():
    file1 = open("file.txt" , "r")
    total = 0
    for line in file1:
        total = total + int(line)
    print(total)
    return total
    file1.close()
main()

