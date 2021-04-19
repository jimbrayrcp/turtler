# ################################
#   Copyright (c) 2021 Jim Bray
#       All Rights Reserved
# ################################
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_start_position()
        self.setheading(90)
        self.pencolor("green")
        self.shapesize(1, 1, 1.2)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def reset_start_position(self):
        self.clear()
        self.goto(STARTING_POSITION)

    def road_crossed(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


if __name__ == "__main__":
    from turtle import Screen
    from time import sleep
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    player = Player()
    game_is_on = True
    while game_is_on:
        sleep(0.1)
        screen.update()
