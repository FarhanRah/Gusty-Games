from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.8

    def bounce_y(self):
        self.y_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    def increase_speed(self):
        if self.speed() < 10:
            self.speed(self.speed() + 1)
        print(self.speed())
