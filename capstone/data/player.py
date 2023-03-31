from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    "Ініціалізація черепашки-гравця"
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    

    def move_forward(self):
        "Рух вперед"
        self.forward(MOVE_DISTANCE)


    def move_backward(self):
        "Рух назад"
        self.backward(MOVE_DISTANCE)


    def next_level(self):
        "Перевірка по Y-координаті чи переходити на наступний рівень"
        if self.ycor() <= FINISH_LINE_Y: 
            self.goto(STARTING_POSITION)