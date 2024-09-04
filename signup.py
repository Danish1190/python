#signup

from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()


cnx = mysql.connector.connect(host="localhost", user="root", password="", database="login")

def register():
    if vars.get() == 1:
        gender = "male"
    elif vars.get() == 2:
        gender = "female"
    else:
        gender = "other"

    cursor = cnx.cursor()
    query = "INSERT INTO form(name, email, gender, country, password) VALUES (%s, %s, %s, %s, %s)"
    data = (txtname.get(), txtemail.get(), gender, cv.get(), txtpass.get())
    cursor.execute(query, data)
    cnx.commit()
    messagebox.showinfo("Success", "Registration successful!")

root.geometry("600x700")
root.title("Registration Form")

title = Label(root, text="sign up", width=15, font=("times new roman",20))
title.place(x=200, y=20)

name = Label(root, text="Enter Name", width=15, font=("times new roman", 20))
name.place(x=20, y=80)
txtname = Entry(root)
txtname.place(x=250, y=80)

email = Label(root, text="Email", width=15, font=("times new roman", 20))
email.place(x=20, y=120)
txtemail = Entry(root)
txtemail.place(x=250, y=120)

gender = Label(root, text="Gender", width=15, font=("times new roman", 20))
gender.place(x=20, y=160)
vars = IntVar()
Radiobutton(root, text="Male", padx=5, variable=vars, value=1).place(x=200, y=160)
Radiobutton(root, text="Female", padx=10, variable=vars, value=2).place(x=280, y=160)
Radiobutton(root, text="Other", padx=15, variable=vars, value=3).place(x=360, y=160)

listofcountry = ["India", "USA", "France", "America", "China"]
cv = StringVar()
droplist = OptionMenu(root, cv, *listofcountry)
droplist.config(width=15)
cv.set("Select country")
country = Label(root, text="Country", width=15, font=("times new roman", 20))
country.place(x=20, y=200)
droplist.place(x=250, y=200)

password = Label(root, text="Password", width=15, font=("times new roman", 20))
password.place(x=20, y=240)
txtpass = Entry(root, show='*')
txtpass.place(x=250, y=240)

btn = Button(root, text="Register", width=10, bg="green", fg="white", relief=GROOVE, command=register)
btn.place(x=250, y=280)

root.mainloop()
