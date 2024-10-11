import tkinter as tk
from time import strftime

def update_time():
    label.config(text=strftime('%H:%M:%S')) 
    label.after(1000, update_time)           

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root)
label.pack()

update_time()

root.mainloop()