from turtle import Turtle, Screen


def turtle_decorator(func):
    def inner_function():
        s = Screen()
        s.setup(1500, 1200)
        t = Turtle()
        t.shape("turtle")
        func(t)
        t.reset()
        t.hideturtle()
        # s.exitonclick()

    return inner_function
