# ################################
#   Copyright (c) 2021 Jim Bray
#       All Rights Reserved
# ################################
from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.setposition(-230, 260)
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        text = f"Levil: {self.score}"
        self.write(text, move=False, align=ALIGN, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset_score(self):
        self.score = 0
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        text = f"GAME OVER"
        self.setposition(0, 0)
        self.write(text, move=False, align="center", font=FONT)


if __name__ == "__main__":
    from turtle import Screen
    from time import sleep
    from player import Player

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    player = Player()
    score = Scoreboard()
    screen.listen()
    screen.onkey(player.move_forward, "Up")

    game_is_on = True
    while game_is_on:
        sleep(0.1)
        screen.update()
        sleep(2)
        score.add_score()

