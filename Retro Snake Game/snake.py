from turtle import Turtle
STARTING_POSITIONS = [(0.0, 0.0), (-20.0, 0.0), (-40.0, 0.0)]

class Snake:

    def __init__(self):
        self.snake_seg = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_seg.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_seg[-1].pos())

    def reset(self):
        for seg in self.snake_seg:
            seg.goto(1000, 1000)
        self.snake_seg.clear()
        self.create_snake()

    def move(self):
        for n in range(len(self.snake_seg) - 1, 0, -1):
            self.snake_seg[n].goto(self.snake_seg[n - 1].pos())
        self.snake_seg[0].forward(20)

    def up(self):
        if self.snake_seg[0].heading() != 270:
            self.snake_seg[0].setheading(90)

    def down(self):
        if self.snake_seg[0].heading() != 90:
            self.snake_seg[0].setheading(270)

    def left(self):
        if self.snake_seg[0].heading() != 0:
            self.snake_seg[0].setheading(180)

    def right(self):
        if self.snake_seg[0].heading() != 180:
            self.snake_seg[0].setheading(0)