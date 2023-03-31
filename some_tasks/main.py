from turtle import Turtle, Screen
from random import randint
import colorgram

timmy = Turtle()
screen = Screen()

def stop():
    "Вихід з гри"
    exit()


def clear():
    "Очищає поле"
    timmy.clear()


def square():
    "Черепашка малює квадрат"
    timmy.fillcolor(*random_color()) # колір заливки
    timmy.begin_fill()
    for _ in range(4):
        timmy.forward(100)
        timmy.left(90)
    timmy.end_fill()


def dush():
    "Черепашка малює штрихову лінію"
    for _ in range(4):
        timmy.left(90)
        for _ in range(10):
            timmy.forward(10)
            timmy.penup()
            timmy.forward(10)
            timmy.pendown()


def different_shapes():
    'Черепашка малює від 9-кутника до 3-кутника підряд'
    sides = 9
    while sides > 2:
        timmy.fillcolor(random_color())
        angle = 360 / sides
        timmy.begin_fill()
        for _ in range(sides):
            timmy.forward(100)
            timmy.left(angle)
        timmy.end_fill()
        sides -= 1


def random_walk():
    'Черепашка рандомно прогулюється по полю'
    walk = ['left', 'right', 'up', 'down']
    timmy.pensize(7)
    steps = int(screen.numinput('', 'Введи кількість кроків'))
    for _ in range(steps):
        choice_random_walk = walk[randint(0, 3)]
        timmy.pencolor(random_color())
        if choice_random_walk == 'left':
            timmy.left(90)
            timmy.fd(50)
        elif choice_random_walk == 'right':
            timmy.right(90)
            timmy.fd(50)
        elif choice_random_walk == 'up':
            timmy.fd(50)
        elif choice_random_walk == 'down':
            timmy.bk(50)


def spirograph():
    'Черепашка малює спіраль'
    timmy.speed(0)
    diameter_of_circle = int(screen.numinput('', 'Введи діаметр круга:'))
    for _ in range(180):
        timmy.pencolor(*random_color())
        timmy.left(2)
        timmy.circle(diameter_of_circle)


def random_color():
    'Вибір рандомного кольору'
    return (randint(0, 255), randint(0, 255), randint(0, 255))


def damien_hirst():
    'Вибирає з картинки задану кількість кольорів та малює свій шедевр'
    extract_colors = colorgram.extract('img/hirst.jpg', 30)
    rgb = []
    timmy.penup()
    timmy.speed(0)
    for color in extract_colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb.append((r, g, b))
    x = -250
    y = -250
    for _ in range(10):
        timmy.goto(x, y)
        for _ in range(10):
            timmy.forward(50)
            timmy.dot(20, rgb[randint(0, len(rgb) - 1)])
        y += 50


def instagram():
    "Малює піктограму інстаграма"
    timmy.hideturtle()
    timmy.speed(0)
    timmy.fillcolor('black') # колір заливки
    timmy.penup()
    timmy.setpos(-150, -150)
    timmy.pendown()
    timmy.begin_fill()
    for _ in range(4):
        timmy.forward(300)
        timmy.circle(30, 90)
    timmy.end_fill()
    timmy.fillcolor('white') # колір заливки
    timmy.penup()
    timmy.setpos(-110, -110)
    timmy.pendown()
    timmy.begin_fill()
    for _ in range(4):
        timmy.forward(220)
        timmy.circle(30, 90)
    timmy.end_fill()
    timmy.fillcolor('black') # колір заливки
    timmy.penup()
    timmy.setpos(-90, -90)
    timmy.pendown()
    timmy.begin_fill()
    for _ in range(4):
        timmy.forward(180)
        timmy.circle(30, 90)
    timmy.end_fill()
    timmy.fillcolor('white') # колір заливки
    timmy.penup()
    timmy.setpos(0, -35)
    timmy.pendown()
    timmy.begin_fill()
    timmy.circle(70)
    timmy.end_fill()
    timmy.fillcolor('white') # колір заливки
    timmy.penup()
    timmy.setpos(85, 95)
    timmy.pendown()
    timmy.begin_fill()
    timmy.circle(20)
    timmy.end_fill()
    timmy.fillcolor('black') # колір заливки
    timmy.penup()
    timmy.setpos(0, -15)
    timmy.penup()
    timmy.begin_fill()
    timmy.circle(50)
    timmy.end_fill()
    

challenge_function = {
    'exit': stop,
    '0': clear,
    '1': square,
    '2': dush,
    '3': different_shapes,
    '4': random_walk,
    '5': spirograph,
    '6': damien_hirst,
    '7': instagram
}


def turtle():
    "Головне меню програми, вибір функції на виконання"
    screen = Screen()
    screen.colormode(255)
    screen.screensize(400, 400)
    while True:
        timmy.pendown()
        timmy.shape('turtle') # форма черепашки
        timmy.color('black') # колір черепашки
        timmy.pencolor('black') # колір лінії
        timmy.pensize(1) # товщина лінії
        timmy.speed(1) # швидкість черепашки
        choice = screen.textinput("Привіт!", "Доступні варіанти:\n"
                                "0. Очистити поле\n"
                                "1. Намалювати квадрат\n"
                                "2. Квадрат зі штриховою лінією\n"
                                "3. Різнокольорові фігури\n"
                                "4. Рандомна прогулка (своя кількість кроків на вибір)\n"
                                "5. Спіраль\n"
                                "6. Картина Damien Hirst\n"
                                "7. Instagram іконка\n"
                                "Введи номер функції: ")
        selected_function = challenge_function.get(choice)
        if selected_function:
            selected_function()
        else:
            print("Invalid choice")

turtle()
