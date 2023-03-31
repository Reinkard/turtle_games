from turtle import Screen
import time
from snake.data.snake import Body
from snake.data.food import Food
from snake.data.scoreboard import Scoreboard

def snake():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snake')
    screen.tracer(0)
    snake = Body()
    food = Food()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkey(snake.left, 'a')
    screen.onkey(snake.right, 'd')
    screen.onkey(snake.up, 'w')
    screen.onkey(snake.down, 's')
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        # detect collision with food
        if snake.head.distance(food) < 20:
            food.refresh()
            scoreboard.eat_food()
            snake.extend()
        # detect collision with wall
        if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
            scoreboard.game_over()
            snake.reset()
        # detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                snake.reset()

snake()
               