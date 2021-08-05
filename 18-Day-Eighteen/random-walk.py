from turtle import Turtle, Screen
from random import choice

tim = Turtle()

colors = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","SlateGray","SeaGreen"]
directions = [0,90,180,270]
tim.pensize(10)
tim.speed("fast")

for _ in range(500):
    tim.color(choice(colors))
    tim.fd(20)
    tim.setheading(choice(directions))

screen = Screen()
screen.exitonclick()