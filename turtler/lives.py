# ################################
#   Copyright (c) 2021 Jim Bray
#       All Rights Reserved
# ################################
from turtle import Turtle
from time import sleep

FONT = ("Courier", 24, "normal")
ALIGN = "center"


class Lives(Turtle):
    def __init__(self):
        super(Lives, self).__init__()
        self.life_count = 3
        self.timer = 5
        self.reset_player = False
        self.start_lifeboard()

    def start_lifeboard(self):
        self.penup()
        self.setposition(230, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        text = f"Lives: {self.life_count}"
        self.write(text, move=False, align=ALIGN, font=FONT)

    def take_one(self):
        self.life_count -= 1
        if self.life_count:
            self.clear()
            self.update_scoreboard()
            self.timer = 5
            self.road_kill()
        else:
            self.clear()
            self.update_scoreboard()
            self.game_over()

    def road_kill(self):
        while self.timer:
            text = f"   ROAD KILL! \n" \
                   f"Restarting in {self.timer}"
            self.setposition(0, 0)
            self.timer -= 1
            self.write(text, move=False, align="center", font=FONT)
            sleep(1)
            self.clear()
            self.start_lifeboard()
        self.reset_player = True


    def reset_off(self):
        self.reset_player = False

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
    score = Lives()
    screen.listen()
    screen.onkey(player.move_forward, "Up")
    game_is_on = True
    while game_is_on:
        sleep(0.1)
        screen.update()
        sleep(2)
        score.take_one()
