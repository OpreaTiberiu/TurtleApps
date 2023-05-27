from turtle import Turtle, Screen
import random
import webcolors


def etch_a_sketch():
    def forward():
        t.forward(10)

    def back():
        t.backward(10)

    def left():
        t.setheading(t.heading() + 10)

    def right():
        t.setheading(t.heading() - 10)

    def clear():
        t.reset()

    s = Screen()
    s.setup(1500, 1200)

    t = Turtle()

    s.listen()
    s.onkey(forward, 'd')

    s.onkey(left, 'w')

    s.onkey(right, 's')

    s.onkey(back, 'a')

    s.onkey(clear, 'c')

    s.onkey(forward, "space")

    s.exitonclick()


if __name__ == "__main__":
    etch_a_sketch()
