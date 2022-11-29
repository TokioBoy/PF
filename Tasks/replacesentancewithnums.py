import string
text = "32rrv32"
alphabet = string.ascii_lowercase
def main():
  for i in text:
    if i in alphabet:
      print(str(ord(i)-96), end=' ')
main()


