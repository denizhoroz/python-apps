from tkinter import *
from tkinter import messagebox
import json
from passwordGenerator import password_gen

FILE_PATH = "apps\\password-manager-start\\password_data.json"
pm_cred_last = ""

def butcom_gen():
    entry_password.delete(0, END)
    password = password_gen()
    entry_password.insert(0, password)


def butcom_search():
    website = entry_website.get()

    try:
        with open(FILE_PATH, "r") as file:
            file_data = json.load(file)
            user_data = file_data[website]
    except KeyError:
        messagebox.showerror(title="Error", message="No data found.")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")
    else:
        user_email = user_data["email"]
        user_password = user_data["password"]
        messagebox.showinfo(title="User information", message=f"Website: {website}\nEmail: {user_email}\nPassword: {user_password}")


def butcom_add():
    user_website = entry_website.get()
    user_credentials = entry_credentials.get()
    user_password = entry_password.get()

    if not (user_website == "" or user_credentials == "" or user_website == ""):
        new_info = {
            user_website: {
                "email": user_credentials,
                "password": user_password
            }
        }

        try:
            with open(FILE_PATH, "r") as file:
                info = json.load(file)
                info.update(new_info)
        except:
            with open(FILE_PATH, "w") as file:
                json.dump(new_info, file, indent=True)
        else:
            with open(FILE_PATH, "w") as file:
                json.dump(info, file, indent=True)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)        
        
        warning_window = Toplevel(window)
        warning_window.config(padx=30, pady=10)
        warning_window.title("Password Manager")
        Label(warning_window, text="Your credentials has been added to the database", font=FONT).pack(expand=True)
        Button(warning_window, text="OK", font=FONT, command=warning_window.destroy).pack(expand=True)
    else:
        warning_window = Toplevel(window)
        warning_window.config(padx=30, pady=10)
        warning_window.title("Password Manager")
        Label(warning_window, text="Please fill the required fields", font=FONT).pack(expand=True)
        Button(warning_window, text="OK", font=FONT, command=warning_window.destroy).pack(expand=True)


window = Tk()
window.title("Password Manager 1.0v")
window.config(padx=20, pady=20)

IMAGE_PATH = "apps\\password-manager-start\\logo.png"
logo_sprite = PhotoImage(file=IMAGE_PATH)
logo_canvas = Canvas(width=200, height=200)
logo_canvas.create_image(100, 100, image=logo_sprite) 

FONT = ("Arial", 10, "normal")
label_website = Label(text="Website:", font=FONT)
label_credentials = Label(text="Email/Username:", font=FONT)
label_password = Label(text="Password:", font=FONT)

entry_website = Entry(width=29)
entry_credentials = Entry(width=50)
entry_password = Entry(width=29)

button_generate = Button(text="Generate Password", font=FONT, command=butcom_gen)
button_add = Button(text="Add", font=FONT, width=40, command=butcom_add)
button_search = Button(text="Search", font=FONT, width=14, command=butcom_search)

logo_canvas.grid(row=0, column=1)
label_website.grid(row=1, column=0)
entry_website.grid(row=1, column=1)
button_search.grid(row=1, column=2)
label_credentials.grid(row=2, column=0)
entry_credentials.grid(row=2, column=1, columnspan=2)
label_password.grid(row=3, column=0)
entry_password.grid(row=3, column=1)
button_generate.grid(row=3, column=2)
button_add.grid(row=4, column=1, columnspan=2)

entry_website.focus()
entry_credentials.insert(0, pm_cred_last)

window.mainloop()
