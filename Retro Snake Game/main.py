from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(500, 500)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Retro Snake Game")

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting if the snake ate the food
    if snake.snake_seg[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()

    # Detecting if the snake hits the wall
    if snake.snake_seg[0].xcor() > 230 or snake.snake_seg[0].xcor() < -230 or snake.snake_seg[0].ycor() > 230 or snake.snake_seg[0].ycor() < -230:
        snake.reset()
        score.reset()

    # Detecting if the head hits the tail
    for segment in snake.snake_seg[1:]:
        if snake.snake_seg[0].distance(segment) < 10:
            snake.reset()
            score.reset()

screen.exitonclick()
