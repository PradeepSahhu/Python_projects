#
# # import another_module
# #
# # print(another_module.another_variable) # It is a variable
#
# # import turtle
# from turtle import Turtle, Screen
#
# timmy = Turtle() #It is a class
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DeepPink3")
# timmy.forward(100.5)
#
# my_screen = Screen()
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

from prettytable import PrettyTable  # importing the class

table = PrettyTable()  # Making a object named table
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])  # Accessing the method of the class
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"  # Changing attribute

print(table)
