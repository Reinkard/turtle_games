from turtle import Turtle
ALIGN = "center"
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open('./snake/data/high_score.txt', 'r') as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.pencolor('white')
        self.goto(0, 250)
        self.write(f'Score is: {self.score}. Max score is {self.high_score}', move=False, align=ALIGN, font=FONT)
    

    def eat_food(self):
        self.clear()
        self.score += 1
        self.write(f'Score is: {self.score}. Max score is {self.high_score}', move=False, align=ALIGN, font=FONT)


    def game_over(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            self.new_high_score()
        self.score = 0
        self.write(f'Score is: {self.score}. Max score is {self.high_score}', move=False, align=ALIGN, font=FONT)
    

    def new_high_score(self):
        with open('./snake/data/high_score.txt', 'w') as f:
            f.write(f'{self.high_score}')