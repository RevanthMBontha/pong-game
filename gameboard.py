from turtle import Turtle

from global_helpers import PADDLE_COLOR, PADDLE_SHAPE, HORIZONTAL_EDGE, VERTICAL_EDGE, ORIGIN, STRETCH_MULTIPLIER


class GameBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor(PADDLE_COLOR)
        self.shapesize(stretch_wid=STRETCH_MULTIPLIER, stretch_len=STRETCH_MULTIPLIER)
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)

    def draw_board(self):
        self.draw_horizontal_line(HORIZONTAL_EDGE, VERTICAL_EDGE)
        self.draw_horizontal_line(HORIZONTAL_EDGE, -1 * VERTICAL_EDGE)
        self.draw_vertical_line()

    def draw_horizontal_line(self, x_cor, y_cor):
        self.setpos(-1 * x_cor, y_cor)
        while self.xcor() <= x_cor:
            self.stamp()
            new_x = self.xcor() + (20 * STRETCH_MULTIPLIER)
            self.setpos(new_x, self.ycor())

    def draw_vertical_line(self):
        """Draws the vertical line on the board"""
        self.setpos(0, VERTICAL_EDGE)
        while self.ycor() >= -1 * VERTICAL_EDGE:
            self.stamp()
            new_y = self.ycor() - (20 * STRETCH_MULTIPLIER)
            self.setpos(self.xcor(), new_y)
            self.stamp()
            new_y = self.ycor() - (40 * STRETCH_MULTIPLIER)
            self.setpos(self.xcor(), new_y)

    def draw_axis(self):
        """Debug function to draw important points on the screen"""
        self.setpos(ORIGIN)
        self.pendown()
        self.setpos(0, 300)
        self.setpos(0, -300)
        self.setpos(ORIGIN)
        self.setpos(-400, 0)
        self.setpos(400, 0)
        self.penup()
        self.setpos(-1 * HORIZONTAL_EDGE, VERTICAL_EDGE)
        print(self.pos())
        self.stamp()
        self.setpos(-1 * HORIZONTAL_EDGE, -1 * VERTICAL_EDGE)
        print(self.pos())
        self.stamp()
        self.setpos(HORIZONTAL_EDGE, VERTICAL_EDGE)
        print(self.pos())
        self.stamp()
        self.setpos(HORIZONTAL_EDGE, -1 * VERTICAL_EDGE)
        print(self.pos())
        self.stamp()
