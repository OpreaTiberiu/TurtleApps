from turtle import Turtle, Screen
import random
import webcolors


def turtle_race():
    s = Screen()
    s.setup(1500, 1200)
    default_pos = (-600, -500)
    racing_turtles = []
    colors = []
    # Setup 8 racing turtles
    for i in range(8):
        racing_turtle = Turtle("turtle")
        racing_turtle.penup()
        racing_turtle.speed("fastest")
        random_rgb_color = random.choice(list(webcolors.CSS3_HEX_TO_NAMES.values()))
        while random_rgb_color in colors:
            random_rgb_color = random.choice(list(webcolors.CSS3_HEX_TO_NAMES.values()))
        colors.append(random_rgb_color)
        racing_turtle.fillcolor(random_rgb_color)
        racing_turtle.goto(default_pos[0], default_pos[1] + i * 150)
        racing_turtle.turtlesize(2, 2)
        racing_turtles.append(racing_turtle)

    # Ask the user to bet on one of the 8 turtles
    user_choice = s.textinput("Who do you want to bet on?", f"The racers are:\n {', '.join(colors)}")

    # Race the turtles and display the winner
    race_on = True
    while race_on:
        for racing_turtle in racing_turtles:
            if race_on:
                racing_turtle.forward(random.randint(20, 50))
                if racing_turtle.pos()[0] >= 700:
                    race_on = False
                    user_won = "WON" if user_choice == racing_turtle.fillcolor() else "LOST"
                    t = Turtle()
                    t.write(f"The winner is {racing_turtle.fillcolor()}. You {user_won}!",
                            font=("Arial", 30, "normal"),
                            align="center")
                    t.hideturtle()
    s.exitonclick()