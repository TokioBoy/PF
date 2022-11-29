def main():
    grade_ipt = (int(input("Enter a number:  ")))
    grades = ("F" * 60 + "D" * 10 + "C" * 10 + "B" * 10 + "A")
    #Создает кучу букв
    print(grades[grade_ipt])
    #Вводишь число и оно выводит буковку
main()

