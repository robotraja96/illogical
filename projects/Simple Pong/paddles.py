from turtle import Turtle

y_coordinate = 0


class Paddle:

    def __init__(self, coordinate):
        self.paddle = Turtle('square')
        self.paddle.color('white')
        self.paddle.turtlesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(coordinate, y_coordinate)


    def up(self):
        self.paddle.setpos(self.paddle.xcor(), self.paddle.ycor() + 20)

    def down(self):
        self.paddle.setpos(self.paddle.xcor(), self.paddle.ycor() - 20)
