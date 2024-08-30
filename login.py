from tkinter import*
from tkinter import messagebox
import mysql.connector

root=Tk()

log=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="login"
)
def loginform():
    name=txtname.get()
    email=txtemail.get()
    password=txtpass.get()
    cursor=log.cursor()
    query = "SELECT *FROM  form WHERE name=%s AND email=%s AND  password=%s"
    cursor.execute(query,(name,email,password))
    row = cursor.fetchone()

    if row ==None:
        messagebox.showerror("Error","Invalid Credentials")
    else:
        messagebox.showinfo("Success","Login Successful")

root.geometry("400x300")
root.title("LOGIN FORM")

lblname=Label(root,text="Name",font=("sans serif",20))
lblname.pack()
txtname=Entry(root)
txtname.pack()

lblemail=Label(root,text="Email",font=("sans serif",20))
lblemail.pack()
txtemail=Entry(root)
txtemail.pack()

lblpass=Label(root,text="Password",font=("sans serif",20))
lblpass.pack()
txtpass=Entry(root)
txtpass.pack()

btn=Button(root,text="login",relief=GROOVE,bg="black",fg="white",command=loginform)
btn.pack()

root.mainloop()