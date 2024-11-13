import tkinter as tk
import random

def show_popup():
    popup = tk.Toplevel(root)
    popup.title("Thanks")
    label = tk.Label(popup,text="Thanks for accepting",font=("times new roman",15))
    label.pack(padx=20,pady=20)
    
def move_button(event):
    x = random.randint(0, 350)
    y = random.randint(0, 350)
    no_button.place(x=x, y=y)   
    
root = tk.Tk()
root.title("instagram: @danish_iqbal_11")
root.geometry("400x400")

question_label= tk.Label(root, text="Do you like me?",font=("times new roman",20))
question_label.pack(pady=20)

yes_button= tk.Button(root,text="yes",font=("arial",12),command=show_popup)
yes_button.pack()

no_button = tk.Button(root,text="no",font=("arial",12))
no_button.pack()

no_button.bind("<Enter>",move_button)

root.mainloop()