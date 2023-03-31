import pandas
from turtle import Turtle, Screen


class States(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.title('Територія України')
        self.screen.setup(width=1200, height=800)
        self.screen.bgpic('./ukraine_states/ukraine.png')
        self.data = pandas.read_csv('./ukraine_states/ukraine.csv')  # open csv-file ukraine.csv
        self.all_states = self.data['state'].to_list()     # create list from csv-file where key is 'state'
        self.count_of_right_states = 0                     # count of right states
        self.count_of_states = len(self.all_states)        # len of list of states
        self.x_cor = 0                                     # start x coor
        self.y_cor = 0                                     # start y coor
        self.speed('fastest')                              # set speed mode
        self.penup()                                       # hide pen
        self.hideturtle()                                  # hide turtle
        while self.count_of_right_states < self.count_of_states:
            self.user_choice = self.screen.textinput(self.text_tittle(), self.text_input())
            self.add_state(self.user_choice)


    def add_state(self, choice):
        # check if user choice is in list of all states
        if choice in self.all_states:
            self.x_cor = int(self.data[self.data['state'] == choice]['x'])
            self.y_cor = int(self.data[self.data['state'] == choice]['y'])
            self.goto(self.x_cor, self.y_cor)
            self.write(choice, font=('Arial', 14, 'bold'))
            self.count_of_right_states += 1
            self.all_states.remove(choice)
        # check another user input 'exit'
        elif choice == 'exit':
            new_data = pandas.DataFrame(self.all_states)  # create database
            new_data.to_csv('./data/states_to_learn.csv') # save create csv files on states_to_learn.csv
            return exit()
    

    def text_tittle(self):
        return f'{self.count_of_right_states}/{self.count_of_states} кількість областей' # tittle on screen.textinput


    def text_input(self):
        return 'Введи назву області України' # input text on screen.textinput

if __name__ == '__main__':
    app = States
    app.mainloop(self=States)