import tkinter as tk
from datetime import datetime

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        birth_date = datetime(year, month, day)
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        result_label.config(text=f"Your age is: {age} years")
    
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

root = tk.Tk()
root.title("Age Calculator")

tk.Label(root, text="Day:").pack(pady=5)
day_entry = tk.Entry(root)
day_entry.pack(pady=5)

tk.Label(root, text="Month:").pack(pady=5)
month_entry = tk.Entry(root)
month_entry.pack(pady=5)

tk.Label(root, text="Year:").pack(pady=5)
year_entry = tk.Entry(root)
year_entry.pack(pady=5)

button = tk.Button(root, text="Calculate Age", command=calculate_age)
button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
