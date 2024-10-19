import tkinter as tk
from tkinter import messagebox

# Function to add item to the listbox
def add_item():
    item = entry.get()  # Get the item from the entry box
    if item:  # If item is not empty
        listbox.insert(tk.END, item)  # Add the item to the listbox
        entry.delete(0, tk.END)  # Clear the entry box
    else:
        messagebox.showwarning("Input Error", "Please enter an item.")

# Function to print the selected item
def print_item():
    selected_items = listbox.curselection()  # Get selected items
    if selected_items:
        for i in selected_items:
            print("Selected item:", listbox.get(i))  # Print selected items
    else:
        messagebox.showinfo("Selection Error", "No item selected.")

# Function to delete the selected item
def delete_item():
    selected_items = listbox.curselection()  # Get selected items
    if selected_items:
        for i in selected_items[::-1]:  # Reverse to avoid index shift
            listbox.delete(i)  # Delete selected items
    else:
        messagebox.showinfo("Selection Error", "No item selected.")

# Main window
root = tk.Tk()
root.title("Listbox Example")

# Entry widget to input items
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Buttons to add, print, and delete items
add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.pack(pady=5)

print_button = tk.Button(root, text="Print Selected Item", command=print_item)
print_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Selected Item", command=delete_item)
delete_button.pack(pady=5)

# Listbox widget to display items
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=40, height=10)
listbox.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
