import time
from turtle import Screen

from game_over import GameOver
from paddle import Paddle
from ball import Ball
from score import Score
from gameboard import GameBoard

from global_helpers import GAME_REFRESH_RATE, LOWER_LIMIT, UPPER_LIMIT, RIGHT_LIMIT, LEFT_LIMIT, HIT_RADIUS, MAX_SCORE
from global_helpers import RIGHT_SCORE_LIMIT, LEFT_SCORE_LIMIT

# Setting up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

# Setting up the Border
game_board = GameBoard()
game_board.draw_board()

# Setting up the scores
# Right Player
player_A_score = Score(x_cor=100, y_cor=200)
# Left Player
player_B_score = Score(x_cor=-100, y_cor=200)

# Setting up the Player Paddles
player_A_paddle = Paddle(x_cor=350, y_cor=0)
player_B_paddle = Paddle(x_cor=-350, y_cor=0)

# Setting up the Ball
ball = Ball()

# Setting up the Game Over Turtle
game_over = GameOver()

# Binding the inputs to keys
screen.onkeypress(key='Up', fun=player_A_paddle.move_up)
screen.onkeypress(key='Down', fun=player_A_paddle.move_down)
screen.onkeypress(key='w', fun=player_B_paddle.move_up)
screen.onkeypress(key='s', fun=player_B_paddle.move_down)

screen.update()

# Game play start
game_in_play = True
while game_in_play:
    time.sleep(GAME_REFRESH_RATE)
    screen.update()

    # Move the ball
    ball.move()

    # Detect collisions with the wall
    if ball.ycor() <= LOWER_LIMIT or ball.ycor() >= UPPER_LIMIT:
        ball.y_bounce()

    # Detect collision with the Right Paddle
    if ((ball.xcor() > RIGHT_LIMIT) and (ball.xcor() < RIGHT_LIMIT + 10)) and (
            (ball.ycor() < player_A_paddle.ycor() + HIT_RADIUS) and (
            ball.ycor() > player_A_paddle.ycor() - HIT_RADIUS)):
        ball.x_bounce()

    # Detect collision with the Left Paddle
    if ((ball.xcor() < LEFT_LIMIT) and (ball.xcor() > LEFT_LIMIT - 10)) and (
            (ball.ycor() < player_B_paddle.ycor() + HIT_RADIUS) and (
            ball.ycor() > player_B_paddle.ycor() - HIT_RADIUS)):
        ball.x_bounce()

    # Logic for Point for Player_B
    if ball.xcor() >= RIGHT_SCORE_LIMIT:
        player_B_score.update_score()
        ball.reset_ball()
        player_A_paddle.reset_paddle(350, 0)
        player_B_paddle.reset_paddle(-350, 0)

    # Logic for Point for Player_A
    if ball.xcor() <= LEFT_SCORE_LIMIT:
        player_A_score.update_score()
        ball.reset_ball()
        player_A_paddle.reset_paddle(350, 0)
        player_B_paddle.reset_paddle(-350, 0)

    # Checking if the score is greater than the limit
    if player_A_score.get_score() == MAX_SCORE or player_B_score.get_score() == MAX_SCORE:
        game_in_play = False

# Game Over Screen
ball.reset_ball()
if player_A_score.get_score() == MAX_SCORE:
    game_over.show_game_over_screen("Player A")
else:
    game_over.show_game_over_screen("Player B")

screen.exitonclick()
