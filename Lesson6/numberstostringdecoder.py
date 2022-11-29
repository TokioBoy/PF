def main():
    numsstr = input("Please enter the Unicode-encode message:  ")
    message = ""
    for i in numsstr.split():
        codeNum = int(i)
        message = message + chr(codeNum)
    print("\nThe decoded message is:", message)
main()
