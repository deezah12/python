from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(5)

colors = ["blue", "green", "yellow", "black", "wheat", "red",
          "orange", "purple", "violet", "indigo"]

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_sides in range(3, 10):
    tim.color(random.choice(colors))
    draw_shape(shape_sides)


# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
#
# for _ in range(200):
#     tim.color(random.choice(colors))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
