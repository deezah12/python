import turtle as turtle_module
import  random

turtle_module.colormode(225)
tim = turtle_module.Turtle()

color_list = [ (43, 2, 176), (79, 253, 174),
               (226, 149, 109), (230, 225, 253), (232, 254, 243),
               (253, 234, 245),]
tim.dot(20, random.choice(color_list))

screen = turtle_module.Screen()
screen.exitonclick()