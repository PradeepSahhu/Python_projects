# using turtle and GUI to make patterns.
# Using Python turtles to make random points.
# Reading Documentation is the key skill in programming

from turtle import Turtle, Screen
import random

tim = Turtle()

# tim.shape("triangle")
tim.color("aqua")



# tim.pen(pencolor="aqua", speed=10, outline=20)


# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)


# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# ============================================ Making shapes =========================================================

# def shapes(shape_angle, shape_no_of_sides):
#     """ To make different shapes from triangle to decagon """
#     for _ in range(shape_no_of_sides):
#         tim.forward(100)
#         tim.right(shape_angle)
#
#
# def change_color(pen_color):
#     """To change pencolor of turtle"""
#     tim.pencolor(pen_color)
#
#
# color_change_number = 0
#
# color = ['blue', 'green', 'purple', 'aqua', 'black', 'orange', 'pink', 'red']
# shaped = {'triangle': 3, 'square': 4, 'pentagon': 5, 'hexagon': 6, 'heptagon': 7, 'octagon': 8, 'nonagon': 9,
#           'decagon': 10}
# for shape in shaped:
#     print(shape)
#     num_of_sides = (shaped[shape])
#     print(num_of_sides)
#     angle = (360 / num_of_sides)
#
#     colors = (color[0 + color_change_number])
#     color_change_number += 1
#     change_color(pen_color=colors)
#     shapes(shape_angle=angle, shape_no_of_sides=num_of_sides)


# ------------------------ Alternative way to make shape sides and choosing color -----------------------------------

# for side in range(3, 11):
#     num_of_sides = side
#     angle = 360 / num_of_sides
#
#     shapes(shape_angle=angle, shape_no_of_sides=num_of_sides)
#     change_color(random.choice(color))

# ======================================== Alternative way but a long way ======================================

# def triangle():
#     for _ in range(3):
#         tim.forward(100)
#         tim.right(120)
#
#
# def square():
#     """To draw the Square shape turtle"""
#     tim.pencolor("red")
#     for _ in range(4):
#         tim.forward(100)
#         tim.right(90)
#
#
# def pentagon():
#     """To draw five sided pentagon"""
#     tim.pencolor("yellow")
#     for _ in range(5):
#         tim.forward(100)
#         tim.right(72)
#
#
# def hexagon():
#     """To draw six sided hexagon"""
#     tim.pencolor("brown")
#     for _ in range(6):
#         tim.forward(100)
#         tim.right(60)
#
#
# def heptagon():
#     """To draw seven sided heptagon"""
#     tim.pencolor("blue")
#     for _ in range(7):
#         tim.forward(100)
#         tim.right(51.429)
#
#
# def octagon():
#     """To draw eight sided octagon"""
#     tim.pencolor("green")
#     for _ in range(8):
#         tim.forward(100)
#         tim.right(45)
#
#
# def nonagon():
#     """To draw nine sided nonagon"""
#     tim.pencolor("silver")
#     for _ in range(9):
#         tim.forward(100)
#         tim.right(40)
#
#
# def decagon():
#     """To draw ten sided decagon"""
#     tim.pencolor("black")
#     for _ in range(10):
#         tim.forward(100)
#         tim.right(36)
#

# triangle()
# square()
# pentagon()
# hexagon()
# heptagon()
# octagon()
# nonagon()
# decagon()

# ======================================== Generating a random walk =======================================
tim.speed(10)
tim.pensize(10)
color = ['cornflowerBlue', 'DarkOrchid', 'IndianRed', 'LightSeaGreen', 'wheat', 'slateGray', 'blue', 'green', 'purple', 'aqua', 'black', 'orange', 'pink', 'red']

# for _ in range(1000):
#     pen_color = random.choice(color)
#     tim.pencolor(pen_color)
#
#     random_number = random.randint(0, 1)
#     if random_number == 1:
#         tim.left(90)
#     else:
#         tim.right(90)
#     tim.forward(40)
# ----------------------- Alternative way -------------------------
directions = [0, 90, 180, 270]
for _ in range(1000):
    pen_color = random.choice(color)
    # tim.pencolor(pen_color)
    tim.color(pen_color)
    # tim.right(random.choice(directions))
    tim.setheading(random.choice(directions))
    tim.forward(40)

screen = Screen()
screen.exitonclick()
