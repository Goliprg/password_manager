from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_gen = list()

    password_gen.extend([str(random.choice(letters)) for _ in range(0, nr_letters)])
    password_gen.extend([str(random.choice(symbols)) for _ in range(0, nr_symbols)])
    password_gen.extend([str(random.choice(numbers)) for _ in range(0, nr_numbers)])


    random.shuffle(password_gen)

    password_combined = "".join(password_gen)
    password_entry.insert(0, string=password_combined)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error!", message= "Please fill up all of the fields")
    else:
        save_ok = messagebox.askokcancel(title="Approve",message=f"These are the details entered:\nwebsite: {website}\nusername: {username}\npassword: {password}")
        if save_ok:
            file = open("data.txt","a")
            file.write(f"{website} / {username} / {password} \n")
            file.close()
            pyperclip.copy(password)
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            username_entry.insert(0, string="andy@gmail.com")
            password_entry.delete(0, END)
            website_entry.focus()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width= 200,height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

website_entry = Entry(width=52)
website_entry.focus()
website_entry.grid(row=1,column=1,columnspan=2,sticky="w")

username_entry = Entry(width=52)
username_entry.insert(0,string="andy@gmail.com")
username_entry.grid(row=2,column=1,columnspan=2,sticky="w")

password_entry = Entry(width=32)
password_entry.grid(row=3,column=1,sticky="w")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2,sticky="w")

add_button = Button(text="Add",width=44,command= save)
add_button.grid(row=4, column=1,columnspan=2,sticky="w")






window.mainloop()