from turtle import Turtle

from global_helpers import PADDLE_COLOR, FONT, ALIGNMENT, FONT_TYPE, FONT_SIZE


class Score(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(x_cor, y_cor)
        self.score = 0
        self.color(PADDLE_COLOR)
        self.write(f"{self.score}", False, align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", False, align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))

    def get_score(self):
        return self.score
