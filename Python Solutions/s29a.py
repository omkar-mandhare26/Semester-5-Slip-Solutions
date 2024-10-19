import tkinter as tk

def calculate_volume():
    radius = float(entry_radius.get())
    
    volume = (4/3) * 3.14 * (radius ** 3)
    label_result.config(text=f"Volume of the sphere: {volume:.2f}")

root = tk.Tk()
root.title("Volume of Sphere Calculator")

label_radius = tk.Label(root, text="Enter the radius of the sphere:")
label_radius.pack(pady=10)

entry_radius = tk.Entry(root, width=20)
entry_radius.pack(pady=5)

button_calculate = tk.Button(root, text="Calculate Volume", command=calculate_volume)
button_calculate.pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack(pady=20)

root.mainloop()
