# GPT
import tkinter as tk
from tkinter import font

def update_font():
    selected_font = font_name_var.get()
    weight = "bold" if bold_var.get() else "normal"
    selected_size = int(font_size_var.get())
    new_font = font.Font(family=selected_font, size=selected_size, weight=weight)
    label.config(font=new_font)

root = tk.Tk()
root.title("Font Style Modifier")

font_name_var = tk.StringVar(value="Arial")
bold_var = tk.BooleanVar()
font_size_var = tk.StringVar(value="12")

label = tk.Label(root, text="Change my style!", font=("Arial", 12))
label.pack(pady=20)

font_name_label = tk.Label(root, text="Font Name:")
font_name_label.pack()

font_name_menu = tk.OptionMenu(root, font_name_var, "Arial", "Courier", "Times New Roman", "Helvetica", "Verdana", command=lambda _: update_font())
font_name_menu.pack()

bold_check = tk.Checkbutton(root, text="Bold", variable=bold_var, command=update_font)
bold_check.pack()

font_size_label = tk.Label(root, text="Font Size:")
font_size_label.pack()

font_size_menu = tk.OptionMenu(root, font_size_var, "10", "12", "14", "16", "18", "20", command=lambda _: update_font())
font_size_menu.pack()

root.mainloop()