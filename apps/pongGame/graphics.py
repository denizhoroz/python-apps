from turtle import Turtle


class StripLine:
    def __init__(self):
        self.head = Turtle()
        self.strips = []

        self.head.shape("square")
        self.head.turtlesize(stretch_wid=1, stretch_len=0.3)
        self.head.color("white")
        self.head.penup()
        self.strips.append(self.head)

    def start_pos(self):
        self.head.goto(x=0, y=-280)

    def create_strip(self):
        self.new_strip = Turtle()
        self.new_strip.shape("square")
        self.new_strip.turtlesize(stretch_wid=1, stretch_len=0.3)
        self.new_strip.color("white")
        # self.new_strip.color("red") # debug
        self.new_strip.penup()

        tail_pos = self.strips[-1].ycor()
        self.new_strip.goto(x=0, y=tail_pos + 35)
        self.strips.append(self.new_strip)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.pencolor("white")

    def update_score(self, score):
        self.write(arg=f"{score}", align="center", font=("Courier", 80, "bold"))

    def set_type(self, type):
        if type == "player":
            self.goto(x=-60, y=170)
        elif type == "opponent":
            self.goto(x=63, y=170)

