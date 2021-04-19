# ################################
#   Copyright (c) 2021 Jim Bray
#       All Rights Reserved
# ################################

from turtle import Turtle
import random

COLORS = ["red", "orange", "khaki3", "green", "blue", "purple", "LightBlue3"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_group = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance_car = random.randint(1, 6)
        borders = (211, 0, 255)
        if random_chance_car == 6:
            new_car = Turtle("square")
            new_car.fillcolor(random.choice(COLORS))
            new_car.penup()
            new_car.pencolor(borders)
            new_car.width(20)
            new_car.pensize(10)
            new_car.shapesize(1, 2, 1)
            range_y = random.randrange(-240, 250, 40)
            new_car.setposition(290, range_y)
            for car in self.car_group:
                if new_car.distance(car) <= 50:
                    new_car.setposition(320, range_y)
            self.car_group.append(new_car)

    def car_automate(self):
        for car in self.car_group:
            car.backward(self.car_speed)

    def new_level(self):
        self.car_speed += MOVE_INCREMENT

    def reset_level(self):
        self.car_speed = STARTING_MOVE_DISTANCE


if __name__ == "__main__":
    from turtle import Screen
    from time import sleep
    screen = Screen()
    screen.colormode(255)
    screen.setup(width=600, height=600)
    screen.tracer(0)
    cars = CarManager()
    counts = 0
    check_val = 75

    game_is_on = True
    while game_is_on:
        counts += 1
        sleep(0.1)
        screen.update()
        cars.create_car()
        cars.car_automate()
        if counts > check_val:
            cars.new_level()
            check_val += 75
        print(f"VALUE: {counts}  LOOKING FOR: {check_val}")
