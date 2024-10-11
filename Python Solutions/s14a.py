import tkinter as tk

root = tk.Tk()
root.title("Calculate Area & Volume of Cylinder")
root.geometry("500x200")

def calculate_area():
    radius = float(radius_entry.get())
    height = float(height_entry.get())
    area = (2 * 3.14 * radius * height) + (2 * 3.14 * radius * radius)
    area_label.config(text=f"Area: {area:.2f}")

def calculate_volume():
    radius = float(radius_entry.get())
    height = float(height_entry.get())
    volume = 3.14 * radius * radius * height
    volume_label.config(text=f"Volume: {volume:.2f}")

radius_label = tk.Label(root, text="Radius:")
radius_label.pack()

radius_entry = tk.Entry(root)
radius_entry.pack()

height_label = tk.Label(root, text="Height:")
height_label.pack()

height_entry = tk.Entry(root)
height_entry.pack()

area_label = tk.Label(root, text="Area:")
area_label.pack()

volume_label = tk.Label(root, text="Volume:")
volume_label.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_area)
calculate_button.pack()

volume_button = tk.Button(root, text="Calculate", command=calculate_volume)
volume_button.pack()

root.mainloop()