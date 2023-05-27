import turtle
import random
import colorgram
from turtle_decorator import turtle_decorator


@turtle_decorator
def hirst_painting(timmy_turtle):
    colorgram_res = colorgram.extract("img.jpg", 30)
    rgb_colors = [(c.rgb.r, c.rgb.g, c.rgb.b)
                  for c in colorgram_res
                  if not (c.rgb.r >= 240 and c.rgb.g >= 240 and c.rgb.b >= 240)]

    turtle.colormode(255)
    timmy_turtle.penup()
    timmy_turtle.speed("fastest")
    timmy_turtle.goto(-500, -500)
    for i in range(10):
        for j in range(10):
            timmy_turtle.dot(50, random.choice(rgb_colors))
            timmy_turtle.forward(110)
        timmy_turtle.setheading(90)
        timmy_turtle.forward(110)
        timmy_turtle.setheading(180)
        timmy_turtle.forward(1100)
        timmy_turtle.setheading(0)