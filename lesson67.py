#Дз  Написать программу угадай число - где комп загадывает случайное число 1 до 20.
# Если данное число меньше загаданного то комп говорит холодно
# Если данное число больше загаданного то комп говорит горячо
# Если данное число равно загаданному то комп говорит ты молодец ты угадал ура!!! и цикл заверщается
# Вывести время пройденной игры!

#модули
from random import randint, sample
import datetime
cash = 500
start = datetime.datetime.now()

while cash !=0:
    try:
        bet = int(input('Введите ставку\n'
                        f'у вас доступно - {cash}: '))
    except:
        print(f'Вводи цифры Алкаш!!!')
        continue

    if cash < bet or bet<1:
        print(f'Ставка не должна быть больше {cash}')
        continue
    comp = [randint(1,6), randint(1,6)]
    user = [randint(1,6), randint(1,6)]

    if sum(comp)>sum(user):
        cash -= bet
        print('вы проиграли!')
    elif sum(comp)<sum(user):
        cash+=bet
        print('Вы выйграли')
    else:
        print('Ничья')

endtime = datetime.datetime.now() - start
print(f'Вы пробыли в игре - {endtime.seconds}секунды\n'
      f'Сейчас время время {datetime.datetime.now()}')









# import turtle
# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while 1:
#     forward(200)
#     left(170)
#     if abs (pos()) < 1:
#         break
# end_fill()




# import random
# from random import randint, choice
# from datetime import datetime, date
# import time
# print(random.randint(1,100))
# guys = ['jack', 'jonson','helena', 'anna', 'qwerty']
# print(choice(guys))




# print(date.today())
# print(date.min)
# print(datetime.now())
#


# from lesson5 import summa as s
#
# print(s(1,3,4))






# #try exept
# while 1:
#     try:
#         first_num = float(input('Введите первое число: '))
#         operation = str(input('+ - / *: '))
#         second_num = float(input('Введите второе число: '))
#     except:
#         print('Пожалуйста вводите только числа!!!')
#
#     if operation == "+":
#         print(f'{first_num} + {second_num} = {first_num+second_num}')
#     elif operation == '-':
#         print(f'{first_num} - {second_num} = {first_num - second_num}')
#
#     elif operation == '*':
#         print(f'{first_num} * {second_num} = {first_num * second_num}')
#
#     elif operation == '/':
#         print(f'{first_num} / {second_num} = {first_num / second_num}')
#
#     exit = str(input('Выйти? да/нет '))
#     if exit =='да':
#         break
#     else:
#         continue
#
#
# # try:
# #     a = '12'
# #     b = '12'
# #     print(a + b)
# # except:
# #     c = 12
# #     m = 12
# #     print(c+m)
#
#
#
#
#
#
#
# # plus1 = lambda x, y: x+y
# # print(plus1(1,3))
#
#
# # def plus(x,y):
# #     return x+y
# # a = plus(1,3)
# # print(a)
# # print(plus(3, 4))