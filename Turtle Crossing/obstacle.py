from turtle import Turtle
from random import randint

class Obstacle:

    def __init__(self):
        self.all_obstacles = []
        self.max_number = 6

    def create(self):
        if randint(0, self.max_number) == 1:
            self.obstacle = Turtle()
            self.obstacle.shape("square")
            self.obstacle.shapesize(1, 2)
            self.obstacle.color(randint(0, 255), randint(0, 255), randint(0, 255))
            self.obstacle.penup()
            self.obstacle.goto(270, randint(-220, 220))
            self.all_obstacles.append(self.obstacle)

    def start_move(self):
        for each in self.all_obstacles:
            each.backward(10)