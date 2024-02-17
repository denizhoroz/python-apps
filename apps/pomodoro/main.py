from tkinter import *
import time
import math


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#90c454"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
chks = 0
timer = None

IMAGE_PATH = "apps/pomodoro/tomato.png"


def reset_timer():
    global reps

    reps = 0
    window.after_cancel(timer)
    tomato_canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")


def start_timer():
    global reps
    reps += 1 

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 1:
        title_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
    else:
        title_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    

def clock_display(time_seconds):
    MINUTES_SEG = math.floor(time_seconds / 60) 
    SECONDS_SEG = time_seconds % 60
    if MINUTES_SEG < 10:
        MINUTES_SEG = f"0{MINUTES_SEG}"

    if SECONDS_SEG == 0:
        SECONDS_SEG = "00"
    elif SECONDS_SEG < 10:
        SECONDS_SEG = f"0{SECONDS_SEG}"

    CLOCK_STRING = f"{MINUTES_SEG}:{SECONDS_SEG}"
    return CLOCK_STRING


def count_down(count):
    global reps

    clock = clock_display(count)
    tomato_canvas.itemconfig(timer_text, text=clock)
    
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        
        mark = ""

        for _ in range(math.floor(reps/2)):
            
            mark += "✔️"
            check_marks.config(text=mark)

        start_timer()


window = Tk()
window.config(padx=100, pady=100, bg=YELLOW)
window.title("Pomodoro")

tomato_canvas = Canvas(width=200, height=225, bg=YELLOW, highlightthickness=0)
tomato_sprite = PhotoImage(file=IMAGE_PATH)
tomato_canvas.create_image(100, 112, image=tomato_sprite)
timer_text = tomato_canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))

title_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 50, "normal"))
button_start = Button(text="Start", command=start_timer)
button_reset = Button(text="Reset", command=reset_timer)
check_marks = Label(text="", fg=GREEN, bg=YELLOW)

title_label.grid(column=1, row=0)
tomato_canvas.grid(column=1, row=1)
button_start.grid(column=0, row=2)
button_reset.grid(column=2, row=2)
check_marks.grid(column=1, row=3)

window.mainloop()
