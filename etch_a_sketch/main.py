from turtle import Turtle, Screen


tim = Turtle(shape='turtle')
screen = Screen()
screen.title('Etch a sketch')
screen.setup(width=500, height=500)


def close_application():
    'Close application'
    exit()


def etch_a_sketch():
    'Etch-A-Scetch'
    screen.listen()
    screen.onkey(key="w", fun=move_forward)
    screen.onkey(key="s", fun=move_backward)
    screen.onkey(key="a", fun=move_left)
    screen.onkey(key="d", fun=move_right)
    screen.onkey(key='c', fun=clear)
    screen.onkey(key='q', fun=close_application)


def move_forward():
    'One step forward'
    tim.forward(10)


def move_backward():
    'One step backward'
    tim.backward(10)


def move_left():
    'Move left'
    tim.left(10)


def move_right():
    'Move right'
    tim.right(10)


def clear():
    'Clear screen'
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

etch_a_sketch()

screen.exitonclick()