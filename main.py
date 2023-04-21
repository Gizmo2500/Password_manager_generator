from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# generates a random password
def generate_password():

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    print(password_list)
    shuffle(password_list)

# "".join(list) concatinates the string list
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    site = web_input.get()
    u_email = user_email_input.get()
    g_password = password_input.get()
    new_data = {site: {"email": u_email,
                       "password": g_password}
                }
    if len(site) == 0 or len(g_password) == 0:
        messagebox.showinfo(title="Missing Information", message="Please make sure \n to fill in all boxes")
    else:
        try:
            with open(file="data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving updated data file
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data file
                json.dump(data, data_file, indent=4)
        finally:
            web_input.delete(0, END)
            password_input.delete(0, END)


# ----------------------------  Search  ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as data_file:
            # Reading data
            data = json.load(data_file)
        website = data[web_input.get()]
    except FileNotFoundError:
        messagebox.showinfo(message="File not Found")
        web_input.delete(0, END)
    except KeyError:
        messagebox.showinfo(message="Website not found. Please check the spelling and try again")
    else:
        messagebox.showinfo(title=web_input.get(), message=f" Email: {website['email']} \n "
                                                           f"Password: {website['password']}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas

canvas = Canvas(width=200, height=200)
lock_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(row=0, column=1)

# Labels Input boxes

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
web_input = Entry(width=22)
web_input.focus()
web_input.grid(row=1, column=1)

user_email_label = Label(text="Email/Username:")
user_email_label.grid(row=2, column=0)
user_email_input = Entry(width=40)
user_email_input.insert(0, "vash2500@gmail.com")
user_email_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_input = Entry(width=22)
password_input.grid(row=3, column=1)

# buttons
search_btn = Button(text="Search", width=12, command=find_password)
search_btn.grid(row=1, column=2)
generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()
