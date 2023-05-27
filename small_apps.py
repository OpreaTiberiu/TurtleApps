import turtle
import random
from turtle_decorator import turtle_decorator


@turtle_decorator
def draw_square(timmy_turtle):
    for _ in range(0, 4):
        timmy_turtle.forward(100)
        timmy_turtle.left(90)


@turtle_decorator
def dashed_line(timmy_turtle):
    timmy_turtle.penup()
    timmy_turtle.goto(-600, 0)
    timmy_turtle.pendown()
    for _ in range(0, 50):
        timmy_turtle.forward(10)
        timmy_turtle.penup()
        timmy_turtle.forward(10)
        timmy_turtle.pendown()


@turtle_decorator
def draw_shapes(timmy_turtle):
    for i in range(3, 12):
        angle = 360 / i
        for _ in range(0, i):
            timmy_turtle.forward(100)
            timmy_turtle.left(angle)


@turtle_decorator
def random_walk(timmy_turtle):
    turtle.colormode(255)
    timmy_turtle.speed("fastest")
    timmy_turtle.width(10)
    for _ in range(0, 100):
        tilt = random.randint(0, 360)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        timmy_turtle.pencolor(color)
        timmy_turtle.left(tilt)
        timmy_turtle.forward(50)
    turtle.colormode(1)


@turtle_decorator
def spirograph(timmy_turtle):
    turtle.colormode(255)
    timmy_turtle.speed("fastest")
    timmy_turtle.width(3)
    for _ in range(120):
        timmy_turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        timmy_turtle.circle(radius=300)
        timmy_turtle.left(3)
    turtle.colormode(1)
