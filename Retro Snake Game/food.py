from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("green")
        self.shapesize(0.75, 0.75)
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-220, 220), random.randint(-220, 220))