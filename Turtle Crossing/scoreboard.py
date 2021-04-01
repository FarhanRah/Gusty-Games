from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-230, 250)
        self.color("white")
        self.update()
        self.hideturtle()

    def update(self):
        self.write(f"Level: {self.level}", False, "center", font=("Arial", 18, "normal"))

    def level_up(self):
        self.level += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", False, "center", font=("Arial", 18, "normal"))
