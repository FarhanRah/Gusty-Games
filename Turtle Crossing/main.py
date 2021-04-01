from turtle import Screen
from snake import Car
from food import Obstacle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Race")
screen.bgcolor("black")
screen.tracer(0)
screen.colormode(255)

car = Car()
obstacle = Obstacle()
level = Scoreboard()

screen.listen()
screen.onkeypress(car.move, 'Up')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Creating a obstacle every 0.1 second and move the ones already created
    obstacle.create()
    obstacle.start_move()

    # Checking if the car has reached the final point
    if car.ycor() >= 250:
        level.level_up()

        if obstacle.max_number > 3:
            obstacle.max_number -= 1

        car.goto(0, -250)

    # Checking if the car has collided with the obstacle
    for each in obstacle.all_obstacles:
        if car.distance(each) < 20:
            level.game_over()
            game_is_on = False

screen.exitonclick()
