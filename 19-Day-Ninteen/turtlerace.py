from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="User Bet", prompt="Enter a color you think will win")
turtle_color = ["red", "green", "blue", "yellow", "purple", "brown"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"congrats! {winning_color} has won!")
            else:
                print(f"Sorry! {winning_color} has won!")
        random_distance = random.randint(0,9)
        turtle.forward(random_distance)


screen.exitonclick()
