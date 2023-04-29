import time
from turtle import Screen

import car_manager
import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Turtle movement
tim = Player()
screen.listen()
screen.onkey(key='w', fun=tim.move_up)
screen.onkey(key='s', fun=tim.move_down)

# Cars
cars = []

# Score-Keeping
scoring = Scoreboard()

loops = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    loops += 1
    if loops % 6 == 0:
        car = CarManager()
        cars.append(car)
        if tim.ycor() > player.FINISH_LINE_Y:
            tim.goto(player.STARTING_POSITION)
            CarManager.speed_meter += car_manager.MOVE_INCREMENT
            scoring.new_score()
    for objects in cars:
        objects.move()
        if tim.distance(objects) < 30:
            tim.goto(player.STARTING_POSITION)
            scoring.game_over()
            game_is_on = False

screen.exitonclick()