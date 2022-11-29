import random
#библиотека рандома
def main2():
        line1 = "Happy birthday to you!"
        line2 = "Happy birthday, dear Fred..."
        line3 = "No birthday Fred , go home"
        r = random.randint(0,3)
        #Создание рандома
        if(r == 2):
                print(line3)
        else:
                print(line1 ,'\n', line1,'\n',line2 , '\n',line1)
main2()
