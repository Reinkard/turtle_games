import time
from turtle import Screen
from capstone.data.player import Player
from capstone.data.car_manager import CarManager
from capstone.data.scoreboard import Scoreboard

def crossing_capstone():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title('Turtle Crossing Capstone')
    screen.tracer(0)
    screen.listen()

    player = Player()
    scoreboard = Scoreboard()
    car_manager = CarManager()

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_manager.create_car()
        car_manager.move_cars()
        screen.onkey(player.move_forward, 'w')
        screen.onkey(player.move_backward, 's')
        scoreboard.level_board()
        if player.ycor() >= 280:
            scoreboard.level_complete()
            player.next_level()
            car_manager.up_speed()
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                scoreboard.game_over()
                game_is_on = False

    screen.exitonclick()

crossing_capstone()