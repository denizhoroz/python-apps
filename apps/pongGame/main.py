from turtle import Screen
from paddle import Paddle, OppPaddle
from ball import Ball, BallSprite
from graphics import StripLine, Scoreboard
import time

RIGHT_ANGLE = 0
LEFT_ANGLE = 180

mainScreen = Screen()
mainScreen.bgcolor("black")
mainScreen.setup(width=1000, height=600)
mainScreen.tracer(0)

player = Paddle()
opponent = OppPaddle()
ball = Ball()
ball_sprite = BallSprite()

# create scoreboard
playerScore = 0
player_score = Scoreboard()
player_score.set_type("player")
player_score.update_score(playerScore)
opponentScore = 0
opponent_score = Scoreboard()
opponent_score.set_type("opponent")
opponent_score.update_score(opponentScore)

# create strip line
strip_line = StripLine()
strip_line.start_pos()
for i in range(20):
    strip_line.create_strip()

# player controls
mainScreen.listen()
mainScreen.onkeypress(fun=player.up_key_press, key="Up")
mainScreen.onkeyrelease(fun=player.up_key_release, key="Up")
mainScreen.onkeypress(fun=player.down_key_press, key="Down")
mainScreen.onkeyrelease(fun=player.down_key_release, key="Down")

# update screen
game_on = True
while game_on:
    mainScreen.update()
    time.sleep(0.03)

    # controlled movement for player
    player.ctrl_up()
    player.ctrl_down()

    # automatic movement for opponent
    opponent.align(ball)

    # ball and ball sprite movement
    ball.move()
    ball_sprite.chase_ball(ball)

    # detect collision with paddles
    if ball.xcor() < 0:
        x_distance = abs(player.xcor() - ball.xcor())
        y_distance = abs(player.ycor() - ball.ycor())
        if x_distance < 24 and y_distance < 48:
            if player.going_up:
                ball.bounce_right(1)
            elif player.going_down:
                ball.bounce_right(-1)
            else:
                ball.bounce_right(0)
    elif ball.xcor() > 0:
        x_distance = abs(opponent.xcor() - ball.xcor())
        y_distance = abs(opponent.ycor() - ball.ycor())
        if x_distance < 24 and y_distance < 48:
            if opponent.ycor() > 230:
                ball.bounce_left(-1)
            elif opponent.ycor() < -230:
                ball.bounce_left(1)
            else:
                ball.bounce_left(0)

    # detect collision with walls
    if ball.ycor() > 280:
        ball.bounce_wall(1)
    elif ball.ycor() < -280:
        ball.bounce_wall(-1)

    # detect scores
    if ball.xcor() < -510:
        opponentScore += 1
        ball.reset_pos()
        ball.setheading(LEFT_ANGLE)
        player.reset_pos()
    elif ball.xcor() > 510:
        playerScore += 1
        ball.reset_pos()
        ball.setheading(RIGHT_ANGLE)
        opponent.reset_pos()

    # update scores
    player_score.clear()
    player_score.update_score(playerScore)
    opponent_score.clear()
    opponent_score.update_score(opponentScore)

mainScreen.exitonclick()
