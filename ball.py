import time
from turtle import Turtle
from global_helpers import PADDLE_COLOR, BALL_SHAPE, ORIGIN, MOVE_AMOUNT
from global_helpers import get_random_heading


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(ORIGIN)
        self.penup()
        self.shape(BALL_SHAPE)
        self.color(PADDLE_COLOR)
        time.sleep(0.5)
        self.setheading(get_random_heading())
        self.x_move = MOVE_AMOUNT
        self.y_move = MOVE_AMOUNT

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1

    def reset_ball(self):
        self.reset()
        self.__init__()
