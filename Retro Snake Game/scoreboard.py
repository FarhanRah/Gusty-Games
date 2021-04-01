from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 220)
        self.write(f"Score: {self.score}, High Score: {self.high_score}", False, "center", font=("Arial", 16, "normal"))
        self.hideturtle()

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", False, "center", font=("Arial", 16, "normal"))

    def reset(self):
        self.clear()
        if (self.score > self.high_score):
            self.high_score = self.score
        self.score = 0
        self.write(f"Score: {self.score}, High Score: {self.high_score}", False, "center", font=("Arial", 16, "normal"))