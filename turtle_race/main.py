from turtle import Turtle, Screen
from random import randint


def turtle_race():
    'Turtle race'
    screen = Screen()
    screen.title('Turtle race')
    screen.setup(width=500, height=500)
    player = Turtle()
    player.hideturtle()
    colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    user_bet = screen.textinput("Make your bet", f"Who will win the race? Enter a colour:\n{' '.join(colours)}")
    x = -230
    y = -175
    all_turtles = []
    for i in range(7):
        timmy = Turtle(shape='turtle')
        timmy.color(colours[i])
        timmy.penup()
        timmy.goto(x, y)
        y += 60
        all_turtles.append(timmy)
    race_run = True
    while race_run:
        for turtle in all_turtles:
            if turtle.xcor() >= 230:
                race_run = False
                if turtle.pencolor() == user_bet:
                    end_race = screen.textinput('You win!', f'{turtle.pencolor()} turtle is win!')
                    screen.onkey(key='q', fun=close_application)
                else:
                    end_race = screen.textinput('You lose!', f'{turtle.pencolor()} turtle is win!')
                while end_race not in ['q', 'a']:
                    end_race = screen.textinput('Write "q" to quit or "a" to play')
                    if end_race == 'q':
                        exit()
            random_distance = randint(0, 10)
            turtle.forward(random_distance)

def close_application():
    'Close application'
    exit()

turtle_race()