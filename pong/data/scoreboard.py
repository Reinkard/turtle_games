from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.write(f'{self.left_score}', move=False, align='center', font=('Arial', 60, 'normal'))
        self.write(f'{self.right_score}', move=False, align='center', font=('Arial', 60, 'normal'))
            

    def add_goal_left(self):
        self.goto(-100, 200)
        self.clear()
        self.write(f'{self.left_score}', move=False, align='center', font=('Arial', 60, 'normal'))
        self.left_score += 1


    def add_goal_right(self):
        self.goto(100, 200)
        self.clear()
        self.write(f'{self.right_score}', move=False, align='center', font=('Arial', 60, 'normal'))
        self.right_score += 1