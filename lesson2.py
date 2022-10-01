#for while
#for от точки а до точки б
#while - бесконечный цикл, пока значени не будет FALSE он будет работать

#Создать бота который будет спрашивать ваше имя возраст и номер паспорта
#Если вам по возрасту нет 18 лет то бот спрашивает зачем вы пришли?
#while if elif else continue break


while 1:
    n1 = float(input('first number - '))
    o = str(input('+:-:*:/ '))
    n2 = float(input('second number - '))

    if o == '+':
        print(f'{n1} + {n2} = {n1+n2}')
    elif o == '-':
        print(f'{n1} - {n2} = {n1+n2}')
    elif o == '*':
        print(f'{n1} * {n2} = {n1*n2}')

    elif o == '/':
        print(f'{n1} + {n2} = {n1/n2}')

    else:
        print('что то пошло не так!!!')
        exit = int(input('Ваш код сломан что будете делать? 1-продолжить 0-выйти '))
        if exit == 1:
            print("Отлично программа заработала приятно поработать !!!")
            continue
        elif exit == 0:
            print('Вы вышли из калькулятора ПОКА!!!!')
            break





# a = 200
# while a != 0:
#     # a = a-1
#     a-=1
#     print('Жазгуль программист!!!')


# for i in 1,2,3,'apple', 'watch', 'python', 'hello':
#     print(f'наши данные из FOR - {i}')

# for i in range(0, 10):
#     print(i+1)


#input() #print() #

#if - 100%
# elif - 50% на 50%
# else - 0%

#>< >= <= == ! or and not


#Дева 23 августа - 21 сентября
# date_birth = int(input('Ваш день рождения? '))
# month = int(input('Ваш месяц рождения? '))
# if date_birth >= 23 and date_birth <= 31 and month == 8 or date_birth <= 21 and month == 9:
#     print('Вы дева!')
# else:
#     print('Вы не дева!')






#купить машину машина стоит 3000$

# cash = int(input('Сколько есть денег на машину? '))
#
# if cash >= 3000:
#     print('Да я куплю себе машину!!!')
#
# elif cash <=2999 and cash>=2500:
#     print('я займу у друга')
#
# elif cash <= 1500 or cash >= 900:
#     print('я буду копить!')
#
# else:
#     print(' я бомж ')


