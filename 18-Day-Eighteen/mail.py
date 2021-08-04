from turtle import Turtle, Screen
from random import choice

tim = Turtle()

colors = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","weat","SlateGray"]
shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']

def draw_shape(number_sides):
    angle = 360 / number_sides
    for _ in range(number_sides):
        tim.fd(100)
        tim.left(angle)
    for _ in range(number_sides):
        tim.fd(100)
        tim.right(angle)

for shape in range(3,11):
    tim.color(choice(colors))
    tim.shape(choice(shapes))
    draw_shape(shape)

screen = Screen()
screen.exitonclick()