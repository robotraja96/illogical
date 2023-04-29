import time
from turtle import Screen

import scoreboard
from scoreboard import Score
from paddles import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Ping Pong Game')
screen.tracer(0)
screen.listen()

# Left paddle and its controls
left_paddle = Paddle(-340)
screen.onkey(key='w', fun=left_paddle.up)
screen.onkey(key='s', fun=left_paddle.down)

# Right paddle and its controls
right_paddle = Paddle(340)
screen.onkey(key='Up', fun=right_paddle.up)
screen.onkey(key='Down', fun=right_paddle.down)

# Ball
ball = Ball()
ball_speed = 0.1

# Score keeping
right_score = Score()
right_score.goto(-150, 200)
left_Score = Score()
left_Score.goto(150, 200)
right_score.update_score()  # Avoids overwriting display of score
left_Score.update_score()

is_game_on = True  # Check to stop while loop
while is_game_on:
    time.sleep(ball_speed)
    screen.update()

    ball.move()

    # Detect collision with wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_move *= (-1)

    # Detect collision with paddle

    if (ball.xcor() == 320 and ball.distance(right_paddle.paddle) < 40) or (
            ball.xcor() == -320 and ball.distance(left_paddle.paddle) < 40):
        ball.x_move *= -1
        ball.speed(ball_speed)
        ball_speed *= 0.9

    # Detect right paddle misses

    if ball.xcor() > 360:
        ball.goto(0, 0)
        ball.x_move *= -1
        left_Score.new_score()
        ball_speed = 0.1

    # Detect left paddle misses

    elif ball.xcor() < -360:
        ball.x_move *= -1
        ball.goto(0, 0)
        right_score.new_score()
        ball_speed = 0.1

    if left_Score.score == 2:
        game_over = Score()
        game_over.pendown()
        game_over.color('Red')
        game_over.penup()
        game_over.write(f'Game over.', True, scoreboard.ALIGNMENT, scoreboard.FONT)

    elif right_score.score == 2:
        game_over = Score()
        game_over.pendown()
        game_over.color('Red')
        game_over.penup()
        game_over.write(f'Game over.', True, scoreboard.ALIGNMENT, scoreboard.FONT)

screen.exitonclick()
