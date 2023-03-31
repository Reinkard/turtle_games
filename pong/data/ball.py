from turtle import Turtle

class Ball(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.speed(1)
        self.setposition(coordinates)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1
        self.move_speed = 0.1


    def move_up(self):
        if self.move_speed > 0.001:
            self.move_speed /= 2
        