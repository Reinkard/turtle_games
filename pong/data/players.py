from turtle import Turtle

class UserPlayer(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0


    def create_player(self, coordinates):
        self.setpos(coordinates)
        self.showturtle()


    def up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)


    def down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 20)


    def center_of_field(self):
        # center line of field
        self.pensize(5)
        self.goto(0, 380)
        self.setheading(270)
        for _ in range(7):
            self.forward(50)
            self.penup()
            self.forward(50)
            self.pendown()
