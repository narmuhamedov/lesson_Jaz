
# import turtle
#
# # Create a playground for turtles
# wn = turtle.Screen()
# wn.bgcolor('skyblue')
#
# # Create turtles
# tess = turtle.Turtle()
# alex = turtle.Turtle()
# henry = turtle.Turtle()
#
#
# def draw_housing():
#     """ Draw a nice housing to hold the traffic lights"""
#     tess.pensize(3)
#     tess.color('black', 'white')
#     tess.begin_fill()
#     tess.forward(80)
#     tess.left(90)
#     tess.forward(157)
#     tess.circle(40, 180)
#     tess.forward(157)
#     tess.left(90)
#     tess.end_fill()
#
#
# draw_housing()
#
#
# def circle(t, ht, colr):
#     """Position turtle onto the place where the lights should be, and
#     turn turtle into a big circle"""
#     t.penup()
#     t.forward(40)
#     t.left(90)
#     t.forward(ht)
#     t.shape('circle')
#     t.fillcolor(colr)
#
#
# circle(tess, 40, 'green')
# circle(alex, 100, 'orange')
# circle(henry, 160, 'red')
#
# # This variable holds the current state of the machine
# state_num = 0
#
#
# def advance_state_machine():
#     global state_num  # The global keyword tells Python not to create a new local variable for state_num
#
#     if state_num == 0:  # Transition from state 0 to state 1
#         henry.color('darkgrey')
#         alex.color('darkgrey')
#         tess.color('green')
#         wn.ontimer(advance_state_machine, 3000)  # set the timer to explode in 3000 milliseconds (3 seconds)
#         state_num = 1
#     elif state_num == 1:  # Transition from state 1 to state 2
#         henry.color('darkgrey')
#         alex.color('orange')
#         wn.ontimer(advance_state_machine, 1000)
#         state_num = 2
#     elif state_num == 2:  # Transition from state 2 to state 3
#         tess.color('darkgrey')
#         wn.ontimer(advance_state_machine, 1000)
#         state_num = 3
#     else:                 # Transition from state 3 to state 0
#         henry.color('red')
#         alex.color('darkgrey')
#         wn.ontimer(advance_state_machine, 2000)
#         state_num = 0
#
# import turtle
# turtle.down()
# turtle.forward(200)
# turtle.left(90)
# turtle.forward(300)
# turtle.left(90)
# turtle.forward(150)
# turtle.left(90)
# turtle.forward(300)
# turtle.up()
# turtle.left(90)
# turtle.forward(60)
# turtle.down()
# turtle.right(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(100)
# turtle.up()
# turtle.forward(70)
# turtle.down()
# turtle.color('green')
# turtle.begin_fill()
# turtle.circle(30)
# turtle.end_fill()
# turtle.up()
# turtle.forward(90)
# turtle.down()
# turtle.color('yellow')
# turtle.begin_fill()
# turtle.circle(30)
# turtle.end_fill()
# turtle.up()
# turtle.forward(90)
# turtle.down()
# turtle.color('red')
# turtle.begin_fill()
# turtle.circle(30)
# turtle.end_fill
# advance_state_machine()
#
# wn.listen()  # Listen for events
#
# wn.mainloop()  # Wait for user to close window
#
#
# #
# #
# # # class OldCar:
# # #     def __init__(self, title, color, cost, comfort):
# # #         self.t = title
# # #         self.clr = color
# # #         self.cst = cost
# # #         self.comfrt = comfort
# # #
# # #     def drive(self, good_bad):
# # #         if good_bad == 'bad':
# # #              return f'This is car - {self.t} dont have comfort {good_bad}'
# # #         elif good_bad == 'good':
# # #             return f'This is car - {self.t}  have comfort {good_bad}'
# # #         else:
# # #             return f'This is car - {self.t} for student'
# # #
# # #     def __str__(self):
# # #         return f'{self.t}\n' \
# # #                f'{self.clr}\n' \
# # #                f'{self.cst}$\n' \
# # #                f'{self.comfrt}'
# # #
# # # oldcar1 = OldCar(title='Жигули', color='yellow', cost=1000, comfort=False)
# # # print(oldcar1)
# # # print(oldcar1.drive(str(input('---'))))
# # #
# # # class NewCar(OldCar):
# # #     def __init__(self, title, color, cost, comfort, abs, airbag, esp):
# # #         super().__init__(title, color, cost, comfort)
# # #         self.abs = abs
# # #         self.airbag = airbag
# # #         self.esp = esp
# # #
# # #     def tunning(self, money):
# # #         return f'Общая цена машины за тюнинг - {self.cst + money}'
# # #
# # #     def __str__(self):
# # #         return super(NewCar, self).__str__()+f'\n{self.abs}\n' \
# # #                                              f'{self.airbag}\n' \
# # #                                              f'{self.esp}'
# # #
# # # newcar1 = NewCar(title='Вольксваген', color='black', cost=5000, comfort=True, abs=True, airbag=True,esp=True)
# # # print(newcar1)
# # # print(newcar1.drive(str(input('---'))))
# # # print(newcar1.tunning(3000))
# #
# #
# # # class Human:
# # #     def __init__(self, name, age, hobby, height, eyes, hair):
# # #         self.n = name
# # #         self.age = age
# # #         self.hobby = hobby
# # #         self.height = height
# # #         self.eyes = eyes
# # #         self.hair = hair
# # #
# # #     def play_games(self, game):
# # #         return f'меня зовут {self.n} Я могу играть в {game}'
# # #
# # #     def __str__(self):
# # #         return f'Имя - {self.n}\n' \
# # #                f'Возраст - {self.age}\n' \
# # #                f'Хобби - {self.hobby}\n' \
# # #                f'Цвет глаз - {self.eyes}\n' \
# # #                f'Цвет волос - {self.hair}'
# # #
# # # human1 = Human(name='Radomir', age=25, hobby='sleep', height=1.84, eyes='brown', hair='black')
# # # print(human1)
# # # print(human1.play_games('CSGO'))
# # # print('-'*50)
# # # human2 = Human(name='Jazgul', age=17, hobby='piano', height=1.60, eyes='brown', hair='brown')
# # # print(human2)
# # # print(human2.play_games('PUBG'))