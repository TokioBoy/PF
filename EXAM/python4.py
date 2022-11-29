def main():
    phrase = input("Enter a phrase: ")
    #creates a variable
    acronym = ""
    #creates a empty variable
    for word in phrase.split():
        acronym = word[0] + acronym
    print(acronym.upper())
     #for each index in the list do the condition
main()