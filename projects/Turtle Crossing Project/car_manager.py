import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10


class CarManager(Turtle):

    speed_meter = STARTING_MOVE_DISTANCE

    def __init__(self):
        super().__init__()
        self.initialize()


    def initialize(self):
        self.shape('square')
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(90)
        self.setpos(250, random.randint(-250, 250))

    def move(self):
        self.setpos(self.xcor() - CarManager.speed_meter, self.ycor())



