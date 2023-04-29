from turtle import Turtle

ALIGNMENT = 'Center'
FONT = ('Courier', 80, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color('Green')
        self.penup()

    def update_score(self):
        self.write(f'{self.score}', True, ALIGNMENT, FONT)

    def new_score(self):
        self.score += 1
        self.clear()
        self.update_score()
