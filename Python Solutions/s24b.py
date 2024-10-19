import tkinter as tk

Numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}


def getEntry():
    input = entry.get()
    words = ""
    for n in input:
        words += f"{Numbers[n]} "

    label.config(text=words)


root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Get Entry", command=getEntry)
btn.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()