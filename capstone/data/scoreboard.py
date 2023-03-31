from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1

    def level_board(self):
        self.goto(-280, 240)
        self.clear()    
        self.write(f'Level: {self.level}', align='left', font=FONT)


    def level_complete(self):
        self.level += 1

    
    def game_over(self):
        self.goto(-100, 0)
        self.clear()    
        self.write('Game over!', align='left', font=FONT)
