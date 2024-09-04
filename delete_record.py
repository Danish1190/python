from tkinter import*
from tkinter import messagebox
import mysql.connector

delete=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="login"
)

root=Tk()
root.title("Delete record")
root.geometry("300x200")

def delete_record():
    id = txtid.get()
    cur=delete.cursor()
    query="DELETE FROM form WHERE id=%s"
    cur.execute(query,(id,))
    delete.commit()
    messagebox.showinfo("Success","Record deleted")
    
lblid=Label(root,text="User id",font=("times new roman",20))
lblid.place(x=100,y=50)
txtid=Entry(root)
txtid.place(x=80,y=80)

btn=Button(root,text="Delete",command=delete_record)
btn.place(x=120,y=120)

root.mainloop()    