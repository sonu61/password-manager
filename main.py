from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website =website_entry.get()
    email = Email_user_name_entry.get()
    password= password_entry.get()
    new_data ={website:{
        "email":email,
        "password":password
    }}

    if len(website)==0  or len(password) == 0:
        messagebox.showerror(title="oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json","r") as data_file:
                #read old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4 )
        else:

            # update data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


#--------------------------Find-Passwors-------------------------------------#
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as datafile:
            data = json.load(datafile)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\n password: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists.")









# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
my_pw_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=my_pw_img)
canvas.grid(row=0,column=1 )

#label
website_label = Label(text="Website: ")
website_label.grid(row=1,column=0)
Email_user_name_label = Label(text="Email/Username: ")
Email_user_name_label.grid(row=2,column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3,column=0)


#entries
website_entry = Entry(width=34)
website_entry.grid(row=1,column=1)
website_entry.focus()
Email_user_name_entry = Entry(width=52)
Email_user_name_entry.grid(row=2,column=1,columnspan=2)
Email_user_name_entry.insert(0,"sonuwww@gmail.com")
password_entry = Entry(width=52)
password_entry.grid(row=3,column=1, columnspan=2)

#button
Generate_password_button = Button(text="Generate Password", command=generate_password)
Generate_password_button.grid(row=3,column=2)

Add_button = Button(text="ADD", width=44, command=save)
Add_button.grid(row=4,column=1,columnspan=2)

Search_btn =Button(text="Search", command=find_password,width=14)
Search_btn.grid(row=1,column=2)


window.mainloop()