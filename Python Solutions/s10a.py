import tkinter as tk
from tkinter import messagebox

def show_alert():
    messagebox.showinfo("Alert", "Button was pressed!")

root = tk.Tk()

alert_button = tk.Button(root, text="Press Me", command=show_alert)
alert_button.pack(pady=20)

root.mainloop()
