from turtle import Turtle, Screen

timmy_the_arrow = Turtle()
timmy_the_arrow.color("blue")


def foward_and_right(right):
    timmy_the_arrow.forward(150)
    timmy_the_arrow.right(right)


def make_shape():
    num = float(1)
    num_shape = 2
    num_deg = 360/num_shape
    num_to_finish = 360/num_deg

    while num <= num_to_finish + 1:
        foward_and_right(num_deg)
        num += 1
        if num > num_to_finish + 1:
            num = 1
            num_deg = 360 / num_shape + 10
            num_to_finish = 360 / num_deg + 3





make_shape()








screen = Screen()
screen.exitonclick()