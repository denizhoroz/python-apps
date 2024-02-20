from tkinter import *
import time as t


# Window configurations
window_width = 260
window_height = 160

# Create window
window = Tk()
window.title("M/Km")
window.geometry(f"{window_width}x{window_height}")
window.resizable(False, False)
window.attributes("-topmost", 1)
window.iconbitmap("apps/mileconv/icon.ico")


# Functions
def update():
    speed = float(entry.get())
    state = switch_state.get()

    if state == 0:
        texts_to_km()
    elif state == 1:
        texts_to_mile()

    if state == 0: ## M to Km
        speed = round(speed * 1.609344, 2)
    elif state == 1: ## Km to M
        speed = round(speed * 0.621371, 2)
    
    result.config(text=f"{speed}")
    

def texts_to_mile():
    entry_label.config(text="kilometers")
    result_label.config(text="miles")


def texts_to_km():
    entry_label.config(text="miles")
    result_label.config(text="kilometers")


# Labels and entries
entry_label = Label(text="miles", font=("Helvatica", 10, "normal"))
entry_label.place(x=180, y=50)

result_label = Label(text="kilometers", font=("Helvatica", 10, "normal"))
result_label.place(x=180, y=80)

filler_label = Label(text="is equal to", font=("Helvatica", 10, "normal"))
filler_label.place(x=36, y=80)

result = Label(text="0", font=("Helvatica", 10, "normal"))
result.place(x=110, y=80)

entry = Entry(width=10)
entry.place(x=110, y=50)

button = Button(text="Calculate", command=update)
button.place(x=110, y=110)

switch_state = IntVar()
switch1 = Radiobutton(text="Mile to Km", value=0, variable=switch_state)
switch2 = Radiobutton(text="Km to Mile", value=1, variable=switch_state)
switch1.place(x=12, y=20)
switch2.place(x=12, y=45)

##
window.mainloop()
