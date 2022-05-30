# using turtle and GUI to make patterns.
# Using Python turtles to make random points.
# Reading Documentation is the key skill in programming

from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
tim.color("aqua")

for _ in range(4):
    tim.forward(100)
    tim.right(90)


screen = Screen()
screen.exitonclick()

