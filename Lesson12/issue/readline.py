def main():
    somefile = open("file.txt" , "r")
    line = somefile.readline()
    while (line != ""):
        line = somefile.readline()
        print(line)
    somefile.close()
main()
input()
  
