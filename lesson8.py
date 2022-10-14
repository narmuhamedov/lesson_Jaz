from random import randint
import datetime

name = input('Как вас зовут?' )
attemps = int(input('Сколько вы хотите попыток? '))
start = datetime.datetime.now()


while 1:
    num1 = randint(1, 9)
    num2 = randint(1, 9)
    action = num1*num2
    print(f'Сколько будет {num1}*{num2}=? ', end='')
    result = int(input("Ваш ответ? "))
    print(action)
    attemps-=1

    with open('results_table_umnoj.txt', 'a', encoding='utf-8') as file:
        if result==action:
            file.write(f'{num1}*{num2}={result} ({action})Правильно!\n')
        elif result!=action:
            file.write(f'{num1}*{num2}={result} ({action})Неправильно!\n')

    if attemps==0:
        d = datetime.datetime.now()-start
        with open('results_table_umnoj.txt','a',encoding='utf-8')as file:
            file.write(
                       f'По времени {d.seconds}\n'
                       f'Ваше имя - {name}')

            break

attemps_u = attemps+1
with open('results_table_umnoj.txt', 'a', encoding='utf-8')as file:
    file.write(f"колличество попыток - {attemps_u}")








# #Запись в файлы
# with open('skiwok.txt', 'r', encoding='utf-8')as stix:
#     print(stix.read())



# #Перезапись файла
# with open('jazgul.txt', 'a', encoding='utf-8')as text:
#     while text!=5:
#         text.write(input('Имена:\n'))
#         print(text)



#Создание текстового файла
# with open('jazgul.txt', 'w', encoding='utf-8') as text:
#     text.write('Привет как дела\n'
#                'Что нового')
#     print(text)



# file = open('skiwok.txt', 'r', encoding='utf-8')
# print(file.read())
# file.close()