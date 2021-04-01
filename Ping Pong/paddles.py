from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.xcor = position[0]
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        if not self.ycor() > 220:
            self.goto(self.xcor, self.ycor() + 20)

    def down(self):
        if not self.ycor() < -220:
            self.goto(self.xcor, self.ycor() - 20)
