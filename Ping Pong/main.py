from turtle import Screen
from snake import Paddle
from food import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.title("Ping Pong Classic")
screen.bgcolor("black")
screen.tracer(0)

player1 = Paddle((-350, 0))
player2 = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(player1.up, 'Up')
screen.onkeypress(player1.down, 'Down')
screen.onkeypress(player2.up, 'w')
screen.onkeypress(player2.down, 's')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Collision of the ball with top or bottom
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Collision of the ball with the paddle
    if (ball.distance(player1) < 50 and ball.xcor() < -320) or (ball.distance(player2) < 50 and ball.xcor() > 320):
        ball.bounce_x()

    # Ball gone outside the range
    if ball.xcor() > 360:
        ball.reset()
        score.add_score1()

    if ball.xcor() < -360:
        ball.reset()
        score.add_score2()

screen.exitonclick()
