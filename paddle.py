from turtle import Turtle
from global_helpers import WIDTH_MULTIPLIER, LENGTH_MULTIPLIER, PADDLE_COLOR, PADDLE_SHAPE, ORIGIN


class Paddle(Turtle):
    def __init__(self, x_cor=0, y_cor=0):
        super().__init__()
        self.penup()
        self.setpos(x_cor, y_cor)
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_wid=WIDTH_MULTIPLIER, stretch_len=LENGTH_MULTIPLIER)

    def move_up(self):
        """Move up the Paddle"""
        if self.ycor() < 240:
            new_y = self.ycor()
            new_y += 20
            self.setpos(self.xcor(), new_y)

    def move_down(self):
        """Move down the Paddle"""
        if self.ycor() > -240:
            new_y = self.ycor()
            new_y -= 20
            self.setpos(self.xcor(), new_y)

    def reset_paddle(self, x_cor, y_cor):
        self.setpos(x_cor, y_cor)
