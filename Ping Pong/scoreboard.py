from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.penup()
        self.goto((-100, 230))
        self.write(f"{self.score1}", False, "center", font=("Arial", 35, "normal"))
        self.goto((100, 230))
        self.write(f"{self.score2}", False, "center", font=("Arial", 35, "normal"))
        self.hideturtle()

    def update(self):
        self.goto((-100, 230))
        self.write(f"{self.score1}", False, "center", font=("Arial", 35, "normal"))
        self.goto((100, 230))
        self.write(f"{self.score2}", False, "center", font=("Arial", 35, "normal"))

    def add_score1(self):
        self.score1 += 1
        self.clear()
        self.update()

    def add_score2(self):
        self.score2 += 1
        self.clear()
        self.update()