from turtle import Turtle
import random as r

UP_ANGLE = 90
SPEED = 12


class Paddle(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=4)
        self.setheading(UP_ANGLE)
        self.color("white")
        self.penup()
        self.going_up = False
        self.going_down = False
        self.goto(x=-450, y=0)

    def up_key_press(self):
        self.going_up = True

    def up_key_release(self):
        self.going_up = False

    def ctrl_up(self):
        if self.going_up and self.ycor() < 250:
            self.forward(SPEED)

    def down_key_press(self):
        self.going_down = True

    def down_key_release(self):
        self.going_down = False

    def ctrl_down(self):
        if self.going_down and self.ycor() > -250:
            self.forward(-SPEED)

    def reset_pos(self):
        self.goto(x=-450, y=0)


class OppPaddle(Paddle):
    def __init__(self):
        super().__init__()

        self.goto(x=450, y=0)

    def align(self, obj_ball):
        y_distance = self.ycor() - obj_ball.ycor()

        if -20 < y_distance < 20:
            pass
        elif y_distance <= -20 and self.ycor() < 250:
            self.forward(SPEED)
        elif y_distance >= 20 and self.ycor() > -250:
            self.forward(-SPEED)

    def reset_pos(self):
        self.goto(x=450, y=0)
