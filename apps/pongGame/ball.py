from turtle import Turtle

RIGHT_ANGLE = 0
RIGHT_UP_BOUNCE = 45
RIGHT_DOWN_BOUNCE = 315
LEFT_ANGLE = 180
LEFT_UP_BOUNCE = 135
LEFT_DOWN_BOUNCE = 225
ACCELERATION = 0.2


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("arrow")
        self.turtlesize(stretch_wid=2, stretch_len=2)
        self.setheading(LEFT_ANGLE)
        self.hideturtle()
        # self.color("DarkMagenta") #debug
        # self.showturtle() #debug
        self.penup()
        self.ballspeed = 16

    def move(self):
        self.forward(self.ballspeed)

    def bounce_right(self, paddle_direction):
        if paddle_direction == 1:
            self.setheading(RIGHT_UP_BOUNCE)
        elif paddle_direction == -1:
            self.setheading(RIGHT_DOWN_BOUNCE)
        else:
            self.setheading(RIGHT_ANGLE)
        self.ballspeed += ACCELERATION

    def bounce_left(self, paddle_direction):
        if paddle_direction == 1:
            self.setheading(LEFT_UP_BOUNCE)
        elif paddle_direction == -1:
            self.setheading(LEFT_DOWN_BOUNCE)
        else:
            self.setheading(LEFT_ANGLE)
        self.ballspeed += ACCELERATION

    def bounce_wall(self, wall_direction):
        if 0 <= self.heading() < 90 or 270 < self.heading() < 360:
            if wall_direction == 1:
                self.setheading(RIGHT_DOWN_BOUNCE)
            elif wall_direction == -1:
                self.setheading(RIGHT_UP_BOUNCE)
        elif 90 < self.heading() < 270:
            if wall_direction == 1:
                self.setheading(LEFT_DOWN_BOUNCE)
            elif wall_direction == -1:
                self.setheading(LEFT_UP_BOUNCE)

    def reset_pos(self):
        self.goto(0, 0)
        self.ballspeed = 16


class BallSprite(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()

    def chase_ball(self, obj_ball):
        xcor = obj_ball.xcor()
        ycor = obj_ball.ycor()

        self.goto(xcor, ycor)
