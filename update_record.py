from tkinter import*
from tkinter import messagebox
import mysql.connector

update= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="login"
)

root=Tk()
root.title("Update Record")
root.geometry("400x300")

def updaterecord():
    query="UPDATE STUDENT SET NAME'"+txtname.get()+"' WHERE EMAIL='"+txtemail.get()+"' where pass="+txtpass.get()+""
    cursor=update.cursor()
    update.commit()
    messagebox.showinfo("SUCCESS","Update")
    
lblname=Label(root,text="Name",font=("times new roman",20))
lblname.pack()
txtname=Entry(root)
txtname.pack()

lblemail=Label(root,text="Email",font=("times new roman",20))
lblemail.pack()
txtemail=Entry(root)
txtemail.pack()

lblpass=Label(root,text="Password",font=("times new roman",20))
lblpass.pack()
txtpass=Entry()
txtpass.pack()   

btn=Button(text="Update",bg="green",fg="black",font="arial")
btn.pack()

root.mainloop() 
