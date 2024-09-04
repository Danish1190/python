from tkinter import *
from tkinter import messagebox
import mysql.connector

update = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="login"
)

root = Tk()
root.title("Update Record")
root.geometry("400x300")

def updaterecord():
    id = txtid.get()
    email = txtemail.get()
    password = txtpass.get()
    cur = update.cursor()
    query="UPDATE form SET email=%s, password=%s WHERE id=%s"
    cur.execute(query,(email,password, id))
    update.commit()
    messagebox.showinfo("success","Record updated")


lblid = Label(root, text="id", font=("times new roman", 20))
lblid.pack()
txtid = Entry(root)
txtid.pack()

lblemail = Label(root, text="Email", font=("times new roman", 20))
lblemail.pack()
txtemail = Entry(root)
txtemail.pack()

lblpass = Label(root, text="Password", font=("times new roman", 20))
lblpass.pack()
txtpass = Entry(root, show="*")  
txtpass.pack()

btn = Button(root, text="Update", bg="green", fg="black", font="arial", command=updaterecord)
btn.pack()

root.mainloop()
