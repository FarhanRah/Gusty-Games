from turtle import Turtle

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, -250)
        self.shape("turtle")
        self.left(90)

    def move(self):
        self.forward(10)