from turtle import Turtle, Screen

def starter_tasks():
    from some_tasks.main import turtle
    turtle()

def states_of_ukraine():
    from ukraine_states.states import States
    states = States()

def turtle_race():
    from turtle_race.main import turtle_race
    turtle_race()

def etch_a_sketch():
    from etch_a_sketch.main import etch_a_sketch
    etch_a_sketch()

def ping_pong():
    from ping_pong.main import ping_pong
    ping_pong()

def snake():
    from snake.main import snake_game
    snake_game()

def crossing_capstone():
    from capstone.main import crossing_capstone
    snake_game()

library = {
    '0': starter_tasks,
    '1': states_of_ukraine,
    '2': turtle_race,
    '3': etch_a_sketch,
    '4': ping_pong,
    '5': snake,
    '6': crossing_capstone,
}


def turtle():
    "Головне меню програми, вибір функції на виконання"
    turtle = Turtle()
    screen = Screen()
    screen.colormode(255)
    screen.screensize(400, 400)
    while True:
        turtle.hideturtle()
        turtle.pendown()
        turtle.shape('turtle') # форма черепашки
        turtle.color('black') # колір черепашки
        turtle.pencolor('black') # колір лінії
        turtle.pensize(1) # товщина лінії
        turtle.speed(1) # швидкість черепашки
        choice = screen.textinput("Hello!",
                                "0. Starter tasks\n"
                                "1. Ukraine States\n"
                                "2. Turtle race\n"
                                "3. Etch a sketch\n"
                                "4. Ping pong\n"
                                "5. Snake\n"
                                "6. Crossing capstone\n"
                                "Input a number: ")
        selected_function = library.get(choice)
        if selected_function:
            selected_function()
        else:
            print("Invalid choice")

turtle()
