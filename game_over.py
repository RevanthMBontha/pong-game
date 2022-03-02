from turtle import Turtle

from global_helpers import PADDLE_COLOR, ALIGNMENT, FONT, FONT_SIZE, FONT_TYPE, ORIGIN, FONT_SIZE_SMALL


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("tomato3")
        self.setpos(0, 25)

    def show_game_over_screen(self, winner):
        self.write("Game Over", False, align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))
        self.setpos(0, -25)
        self.write(f"{winner} won the game", False, align=ALIGNMENT, font=(FONT, FONT_SIZE_SMALL, FONT_TYPE))

