from turtle import Turtle, Screen, colormode
from random import choice, randint

## code for extracting colors from an image
# import colorgram
# rgb_color = []
# colors = colorgram.extract('img/image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b) 
#     rgb_color.append(new_color)
# print(rgb_color)

tim = Turtle()
colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(213, 157, 99), (130, 165, 188), (59, 102, 141), (172, 69, 37), (234, 208, 105), (131, 176, 148), (66, 115, 85), (221, 70, 101), (232, 70, 44), (206, 129, 151), (13, 42, 63), (150, 66, 87), (175, 22, 12), (167, 146, 61), (83, 156, 114), (63, 40, 23), (157, 25, 36), (239, 158, 174), (161, 210, 197), (23, 52, 39), (30, 87, 57), (241, 167, 155), (21, 60, 124), (110, 120, 161), (69, 38, 46), (176, 189, 214)]

tim.setheading(225)
tim.fd(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots +1):
    tim.dot(20, choice(color_list))
    tim.fd(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()