import random

# Paddle Related Stuff
WIDTH_MULTIPLIER = 5
LENGTH_MULTIPLIER = 1

PADDLE_COLOR = 'white'
PADDLE_SHAPE = 'square'


# Ball related stuff
BALL_SHAPE = 'circle'
MOVE_AMOUNT = 12
ORIGIN = (0, 0)

HEADINGS = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 270, 275, 280, 285, 290, 295, 300, 305, 310, 315, 320, 325, 330, 335,
            340, 345, 350, 355]


# Main related stuff
GAME_REFRESH_RATE = 1 / 20

LOWER_LIMIT = -275
UPPER_LIMIT = 275

RIGHT_LIMIT = 340
LEFT_LIMIT = -340

HIT_RADIUS = 50

RIGHT_SCORE_LIMIT = 410
LEFT_SCORE_LIMIT = -410


# Score related stuff
ALIGNMENT = 'center'

FONT = 'Courier'
FONT_TYPE = 'bold'
FONT_SIZE = 48
FONT_SIZE_SMALL = 30

MAX_SCORE = 11


# Board related stuff
HORIZONTAL_EDGE = 390
VERTICAL_EDGE = 290

STRETCH_MULTIPLIER = 0.5


def get_random_heading():
    return random.choice(HEADINGS)
