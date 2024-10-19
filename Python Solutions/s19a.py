import tkinter as tk
from tkinter import messagebox

def display_table():
    try:
        number = int(entry.get())  
        result_text = f"Multiplication Table of {number}:\n\n"
        for i in range(1, 11):
            result_text += f"{number} x {i} = {number * i}\n"
        result_label.config(text=result_text) 
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid integer.")

root = tk.Tk()
root.title("Multiplication Table")

instruction_label = tk.Label(root, text="Enter a number:")
instruction_label.pack(pady=10)

entry = tk.Entry(root, width=20)
entry.pack(pady=5)

button = tk.Button(root, text="Show Table", command=display_table)
button.pack(pady=10)

result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=20)

root.mainloop()
