from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

# Scoreboard
score = Score()

# Paddles
r_paddel = Paddle((350, 0))
l_paddel = Paddle((-350, 0))

# Ball
ball = Ball()

# Controls
screen.listen()
screen.onkey(r_paddel.go_up, "Up")
screen.onkey(r_paddel.go_down, "Down")
screen.onkey(l_paddel.go_up, "w")
screen.onkey(l_paddel.go_down, "s")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.ball_moves()

    # Bounce on top/bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Bounce on paddle
    if (ball.distance(r_paddel) < 50 and ball.xcor() > 320) or (ball.distance(l_paddel) < 50 and ball.xcor() < -320):
        ball.paddle_bounce()

    # Missed right paddle
    if ball.xcor() > 380:
        ball.reset_ball()
        score.l_point()

    # Missed left paddle
    if ball.xcor() < -380:
        ball.reset_ball()
        score.r_point()

screen.exitonclick()
