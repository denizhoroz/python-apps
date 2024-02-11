from turtle import Turtle, Screen
import random as r

mainScreen = Screen()
is_race_on = False
mainScreen.setup(width=500, height=400)
user_bet = mainScreen.textinput(title="Enter your bet", prompt="Which turtle will win the race? Enter a colour: ")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
racer_list = []


def arrange(obj_racer, color_number, x_pos, y_pos):
    obj_racer.color(colors[color_number])
    obj_racer.penup()
    obj_racer.goto(x=x_pos, y=y_pos)


for i in range(6):
    new_racer = Turtle(shape="turtle")
    arrange(obj_racer=new_racer, color_number=i, x_pos=-230, y_pos=(75 - (i * 30)))
    racer_list.append(new_racer)

if user_bet:
    is_race_on = True

while is_race_on:
    for racer in racer_list:
        racer.forward(r.randint(1, 10))
        if racer.xcor() > 230:
            winner = racer.color()
            is_race_on = False
            break

if winner[0] == user_bet:
    print(f"{winner[0]} finished first, you won.")
else:
    print(f"{winner[0]} finished first, you lost.")


mainScreen.exitonclick()
