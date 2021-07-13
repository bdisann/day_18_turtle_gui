from turtle import Turtle, Screen

timmy_the_arrow = Turtle()
timmy_the_arrow.color("blue")

def foward_and_right():
    timmy_the_arrow.forward(100)
    timmy_the_arrow.right(90)

def make_square():
    num = 1
    while num < 5:
        foward_and_right()
        num += 1

make_square()








screen = Screen()
screen.exitonclick()