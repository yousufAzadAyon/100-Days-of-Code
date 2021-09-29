from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My snake game")

start_position = [(0,0), (-20,0), (-40,0)]

for position in start_position:
    snakes = Turtle(shape="square")
    snakes.color("white")
    snakes.goto(position)

screen.exitonclick()