from turtle import Turtle, Screen, colormode
from random import choice, randint

tim = Turtle()
colormode(255)
tim.hideturtle()
tim.speed("fastest")

#colors = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","SlateGray"]
shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']


def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color = (r,g,b)
    return color


def draw_shape(number_sides):
    angle = 360 / number_sides
    tim.width(5)
    for _ in range(number_sides):
        tim.fd(100)
        tim.left(angle)
    for _ in range(number_sides):
        tim.fd(100)
        tim.right(angle)

for shape in range(3,11):
    tim.color(random_color())
    draw_shape(shape)

screen = Screen()
screen.exitonclick()