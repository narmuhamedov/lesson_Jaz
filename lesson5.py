univer = []
technikum = []
army = []
married = []

abiturients = [
    {"name": "Aziz", "ORT": 110, 'gender': 'male'},
    {"name": "KyzSaikal", "ORT": 110, 'gender': 'female'},
    {"name": "Jamin", "ORT": 80, 'gender': 'male'},
    {"name": "Chyngyz", "ORT": 70, 'gender': 'male'},
    {"name": "Jazgul", "ORT": 200, 'gender': 'female'},
    {"name": "Aidar", "ORT": 10, 'gender': 'male'},
    {"name": "John", "ORT": 0, 'gender': 'male'},
    {"name": "Elena", "ORT": 20, 'gender': 'female'},
    {"name": "Azima", "ORT": 10, 'gender': 'female'},
]

def all_abit(lst):
    for i in lst:
        for keys, values in i.items():
            print(f'{keys}-{values}')

def selection(lst, univer:list, technikum:list, army:list, married:list):
    for i in lst:
        if i['ORT'] >= 110:
            univer.append(i)
        elif i['ORT']<=109 and i['ORT']>=45:
            technikum.append(i)

        elif i['ORT']<45 and i['gender']=='male':
            army.append(i)

        elif i['ORT'] < 45 and i['gender'] == 'female':
            married.append(i)


selection(abiturients, univer, technikum, army, married)
print('*'*10)
print(f'В универ пошли - {univer}\n'
      f'В коллеж пошли - {technikum}\n'
      f'В армию ушли - {army}\n'
      f'Замуж вышли - {married}')


#функции-def - некая формула в программировании
# def menu(**kwargs):
#     return kwargs
#
# monday = menu(breakfast='яйичница', lunch='Бивштекс', dinner='Пельмени')
# for k, v in monday.items():
#     print(f'{k}-{v}')




# def about_my_self(*facts):
#     return f'My name is {facts}\n' \
#            f"I'm {facts}\n" \
#            f"My hobby is {facts}\n" \
#            f"My favourite music is {facts}"
#
# about = about_my_self(
#                       str(input('Как вас зовут? ')),
#                       int(input('Сколько вам лет? ')),
#                       str(input('Какое у вас хобби? ')),
#                       str(input('Ваша любимая музыка? '))
#
#                       )
# print(about)



# def average(*temperature):
#     return sum(temperature)/len(temperature)
#
# oblast = average(float(input()), float(input()), float(input()), float(input()),
#               float(input()), float(input()), float(input()))
#
#
# print(f'{round(oblast,2)}')




# def summa(a,b,c):
#     return a+b+c/2
#
# print(summa(1,3,4))fffffcdcdsc


# def greeting(surname, name):
#     return f'{surname}-{name}'
#
# print(greeting("Radomir", "Jazgul"))





# while 1:
#     def greeting(name):
#         print(f'Привет {name.capitalize()}')
#     greeting(input('как вас зовут? '))


#аргумент по умолчанию
# def plus(a,b=12):
#     print(a+b)
#
# plus(12, 33)



# def summa_number(a, b, c, d, e):
#     print(a+b+c+d+e)
#
# summa_number(1, 3, 1, 3, 1)
# summa_number(3, 21.12, 12, 2, 3)
# summa_number(123, 123, 12, 33, 12)


# a = 12
# b = 12
# print(a+b)
#
# v = 12
# m = 12
# print(v+m)
