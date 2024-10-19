import tkinter as tk

def count():
    str = strEntry.get()
    ch = chEntry.get()
    
    count = 0
    for char in str:
        if char == ch:
            count += 1
    
    label.config(text=f"Number of {ch} in {str}: {count}")

root = tk.Tk()

strEntry = tk.Entry(root)
strEntry.pack(pady=10, padx=10)

chEntry = tk.Entry(root)
chEntry.pack(pady=10, padx=10)

btn = tk.Button(root, text="Count", command=count)
btn.pack(pady=10, padx=10)

label = tk.Label(root, text="")
label.pack(pady=10, padx=10)

root.mainloop()