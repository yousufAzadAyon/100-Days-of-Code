from turtle import Turtle, Screen, colormode
from random import choice, randint

tim = Turtle()
colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color = (r,g,b)
    return color

directions = [0,90,180,270]
tim.pensize(10)
tim.speed("fast")

for _ in range(500):
    tim.color(random_color())
    tim.fd(20)
    tim.setheading(choice(directions))

screen = Screen()
screen.exitonclick()