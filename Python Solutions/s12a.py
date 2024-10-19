import tkinter as tk
from tkinter import font

# Function to update label font
def update_font():
    # Get the selected font name, size, and bold option
    selected_font = font_name_var.get()
    selected_size = int(font_size_var.get())
    weight = "bold" if bold_var.get() else "normal"
    
    # Update the label's font with the selected options
    new_font = font.Font(family=selected_font, size=selected_size, weight=weight)
    label.config(font=new_font)

# Create the main window
root = tk.Tk()
root.title("Font Style Modifier")

# Create variables to store the user's selection for font name, size, and bold
font_name_var = tk.StringVar(value="Arial")
font_size_var = tk.StringVar(value="12")
bold_var = tk.BooleanVar()

# Create a label that will display text
label = tk.Label(root, text="Change my style!", font=("Arial", 12))
label.pack(pady=20)

# Create a dropdown menu to select the font name
font_name_label = tk.Label(root, text="Font Name:")
font_name_label.pack()

font_name_menu = tk.OptionMenu(root, font_name_var, "Arial", "Courier", "Times New Roman", "Helvetica", "Verdana", command=lambda _: update_font())
font_name_menu.pack()

# Create a dropdown menu to select the font size
font_size_label = tk.Label(root, text="Font Size:")
font_size_label.pack()

font_size_menu = tk.OptionMenu(root, font_size_var, "10", "12", "14", "16", "18", "20", command=lambda _: update_font())
font_size_menu.pack()

# Create a checkbutton to enable or disable bold text
bold_check = tk.Checkbutton(root, text="Bold", variable=bold_var, command=update_font)
bold_check.pack()

# Start the Tkinter event loop
root.mainloop()
