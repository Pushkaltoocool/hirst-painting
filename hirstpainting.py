from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.speed('fastest')
timmy.up()
timmy.setposition(-200.0,-200.0)

screen = Screen()
screen.colormode(255)

colours = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49)]

def random_colour():
    return colours[random.choice(range(0, len(colours)))]


def draw_hirst():

    for i in range(0,10):
        timmy.dot(20,random_colour())
        timmy.forward(50)
    timmy.setx(-200)
    timmy.left(90)
    timmy.forward(50)
    timmy.right(90)


for i in range(0,10):
    draw_hirst()

screen.exitonclick()