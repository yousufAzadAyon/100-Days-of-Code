from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
for _ in range(4):
    timmy_the_turtle.fd(100)
    timmy_the_turtle.left(90)

screen = Screen()
screen.exitonclick()