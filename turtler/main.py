# ################################
#   Copyright (c) 2021 Jim Bray
#       All Rights Reserved
# ################################
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from lives import Lives

screen = Screen()
screen.title("Turtler")
screen.colormode(255)
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
cars = CarManager()
lives = Lives()
screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.car_automate()

    # DETECT ROADKILL
    for car in cars.car_group:
        if player.distance(car) < 25:
            game_is_on = False
            lives.take_one()
            cars.reset_level()
            if not lives.life_count == 0:
                score.reset_score()

    # HANDLE LIVES
    if lives.reset_player:
        player.reset_start_position()
        game_is_on = not game_is_on
        lives.reset_player = not lives.reset_player

    # DETECT SAFE CROSSING
    if player.road_crossed():
        player.reset_start_position()
        score.add_score()
        cars.new_level()

screen.exitonclick()
