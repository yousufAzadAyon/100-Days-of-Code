from turtle import Turtle, Screen, colormode
from random import randint

tim = Turtle()
tim.shape("arrow")
colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color = (r,g,b)
    return color


tim.speed("fastest")


def draw_sporograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)


draw_sporograph(5)

screen = Screen()
screen.exitonclick()