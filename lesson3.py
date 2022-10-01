a = [1, 2, 3, 'hello', '123']
b = []
c = []
for i in a:
    if type(i) == str:
        b.append(i)
    else:
        c.append(i)
print(b)
print(c)

#list (список) tuple(кортеж)

# nominal = (1, 3, 5, 10, 20, 50, 100, 200, 500, '1k', '2k', '5k')
# nominal = list(nominal)
# nominal.append('hello')
# nominal = tuple(nominal)
#
# print(type(nominal))
# print(nominal.index('2k'))
# print(nominal.count(500))
# print(nominal)

#-----------------------------------------------------------------------

# data_types = [1, 2, 3, 4]
# data_types2 = []
# data_types2.append(data_types.pop(0))
# data_types2.append(data_types.pop(0))
# print(f'второй список - {data_types2}')


# data_types2 = ['hello', 'word']
# data_types2.extend(data_types)
# print(data_types2)




# data_word = 'Radomir'
# data_word = list(data_word)
# data_word.reverse()
# print(data_word)
#
# data_num = [2,31,12,323,4324,1,45,6,7,7,44, 2, 3,3]
# data_num.sort()
# print(data_num)



# data_types = ['hello', 123, 'world', 6, True, 12.33, False, 3.1, 32,'hello']
#
# #списки можно изменять добавлять и удалять
# print(data_types.count('hello')) #показывает колличество элементов в списке
# print(data_types.index(123))
#
#
# #изменение списка
# # data_types[0] = 'qwerty'
# # data_types[2] = 6
# # data_types[3] = 'world'
#
#
#
#
# #2 метода добавления
# # data_types.append('Jazgul')
# # data_types.insert(1, 'INAI')
#
# #2 метода удаления
# # data_types.remove('world')
# # del data_types[0]
#
#
# print(type(data_types))
# print(data_types)
