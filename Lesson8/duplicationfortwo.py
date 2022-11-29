def happy():
    print("Happy birthday to you!")
    #Функция выводящяя этот принт
def sign(person):
    happy()
    happy()
    print("Happy birthday, dear" , person + ".")
    happy()
    #функция выводит 3 предыдущих функции и принтит строку и вставляет имя 
def main():
    sign("Fred")
    print()
    sign("Lucy")
    #Подставляет имя в предыдущуюю функцию и выводит
main()
