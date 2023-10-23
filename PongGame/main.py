from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

def end_game():
    global isGameOn
    isGameOn = False

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

lPaddle = Paddle((-350, 0))
rPaddle = Paddle((350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(rPaddle.goUp, "Up")
screen.onkey(rPaddle.goDown, "Down")
screen.onkey(lPaddle.goUp, "w")
screen.onkey(lPaddle.goDown, "s")
screen.onkey(end_game, 'x')

isGameOn = True
while isGameOn:
    time.sleep(ball.moveSpeed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    # Detect collision with Paddle
    if (ball.distance(rPaddle) < 50 and ball.xcor() > 320) or (ball.distance(lPaddle) < 50 and ball.xcor() < -320):
        ball.bounceX()

    # Detect when the rPaddle misses
    if ball.xcor() > 380:
        ball.resetPosition()
        scoreboard.lPoint()

    # Detect when the lPaddle misses
    if ball.xcor() < -380:
        ball.resetPosition()
        scoreboard.rPoint()

# screen.exitonclick()
