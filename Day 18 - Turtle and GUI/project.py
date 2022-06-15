# import colorgram
#
# # for Extracting colors from an image
#
# colors = colorgram.extract('images.jpg', 30)
# rgb_list = []
# # print(colors)
# for color in colors:
#     # print(color)
#     # print(color.rgb)
#     red = color.rgb.r  # or rgb[0]
#     green = color.rgb.g  # or rgb[1]
#     blue = color.rgb.b  # or rgb[2]
#     # print(red, green, blue)
#     # Red = color.rgb.r  # Alternatively could use this for red
#     # Green = color.rgb.g  # Alternatively could use this for green
#     # Blue = color.rgb.b  # Alternatively could use this for blue
#     color_tuple = (red, green, blue)
#     rgb_list.append(color_tuple)
#
#
# print(rgb_list)
import turtle
import turtle as turtle_module
from random import choice

color_list = [(235, 234, 231), (234, 229, 231), (236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35),
              (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195),
              (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112),
              (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23), (21, 188, 230), (238, 169, 157),
              (162, 210, 182), (138, 210, 232), (0, 123, 54), (88, 130, 182), (180, 187, 211)]

turtle_module.colormode(255)

tim = turtle_module.Turtle()
tim.speed("fastest")

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)

tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# ============================ Alternative way = my Way ===========================
# def dotting():
#     for _ in range(10):
#         tim.dot(20, choice(color_list))
#         tim.penup()
#         tim.forward(50)
#         tim.pendown()
#
#
# for _ in range(10):
#     dotting()
#     tim.penup()
#     tim.left(90)
#     tim.forward(50)
#     tim.setheading(180)
#     tim.forward(500)
#     tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
