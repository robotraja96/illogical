from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('black')
        self.penup()
        self.goto(-200, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f'Level: {self.score}', False, 'center', FONT)

    def new_score(self):
        self.score += 1
        self.clear()
        self.update_score()


    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f'GAME OVER', False, 'center', FONT)