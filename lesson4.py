#Set
# pizza = {'тесто', "колбаса", "сыр", "оливки", "специи", "соус"}
# ramen = {'лапшa', "яйцо", "колбаса", "сыр", "специи", "соус", "мясо"}
# #находит похожее значение
# print(pizza.intersection(ramen))
#
# #микс значений
# print(pizza.union(ramen))
#
# #Не совпадает со значениями
# print(pizza.difference(ramen))
#
# #вывод не одинаковых значений
# print(pizza.symmetric_difference(ramen))



# #словари dict
# nominal = [1, 3, 5, 10, 20, 50, 100, 200, 500, 1000, 2000]
# person = ['nothing', 'nothing', 'nothing', 'nothing', 'Т.Молдо', 'Курманжан Д.',
#           'Т.Сатылганов', 'Осмонов А.', 'Каралаев', 'Баласагын', 'EST FOTO', 'Burana']
#
# banknotes = dict(zip(nominal, person))
# for keys, values in banknotes.items():
#     print(f'{keys}-{values}')
# print(banknotes)




# car = dict(marka="LEXUS", model='RX350', volume=3.0, color='black', date=2003)
#
# for keys, values in car.items():
#     print(f'{keys}:{values}')



# auto2 = car.copy()
# print(car)

#Расширение

#добавление
# car.update(crashtest='very good')

#изменение
# car.update(date=2001)
# print(car.get('marka'))
# print(car.keys())
# print(car.values())
# print(car)


# student = {
#     'name': 'Radomir',
#     'age': 25,
#     1997: 'cow year',
#     'education': True,
#     'height': 1.84,
#     False: 'Married',
#     'telefon number': ['0550644770', '0777111222']
# }
#
# #Изменение
# student['age'] = 26
#
# #Удаление
# del student[1997]
#
# #Добавление
# student['signzodiak'] = 'Virgo'
# student['live'] = 'holost'
#
# print(student)
#


#print(student['telefon number'][1])#Получение из словаря со списка второго значения