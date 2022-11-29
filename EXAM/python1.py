def main():
    lst = ['My', 'Name', 'Is', 'Vladyslav']
    #creates a list
    longest = 0
    for i in lst:
        if len(i) > longest:
            longest = len(i)
    #For each index in list , if index bigger then var "longest" => longest = index
    for i in lst:
        print(i.rjust(longest))
        #for each index in list print index with rjust function
main()
