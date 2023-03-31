from pong.data.players import UserPlayer
from pong.data.ball import Ball
from pong.data.scoreboard import Scoreboard
from turtle import Screen
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title('Ping-Pong')
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

center = UserPlayer()
center.center_of_field()

score = UserPlayer()

player1 = UserPlayer()
player1.create_player((-380, 0))
screen.onkey(fun = player1.up, key='w')
screen.onkey(fun = player1.down, key='s')

player2 = UserPlayer()
player2.create_player((380, 0))
screen.onkey(fun = player2.up, key='Up')
screen.onkey(fun = player2.down, key='Down')

player1_score = Scoreboard()
player1_score.add_goal_right()
player2_score = Scoreboard()
player2_score.add_goal_left()

ball = Ball((0, 0))

def ping_pong():
    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed) # set balls speed
        screen.update()
        ball.move()
        # bounce from y coordinates
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        # bounce from players
        if ball.distance(player2) < 50 and ball.xcor() > 350:
            ball.bounce_x()
            ball.move_up()
        if ball.distance(player1) < 50 and ball.xcor() < -350:
            ball.bounce_x()
            ball.move_up()
        # goal to enemy player
        if ball.xcor() > 380:
            player2_score.add_goal_left()
            ball.goto(0, 0)
            ball.bounce_x()
        elif ball.xcor() < -380:
            player1_score.add_goal_right()
            ball.goto(0, 0)
            ball.bounce_x()


ping_pong()
