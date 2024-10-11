import tkinter as tk

def checkPrime():
    num = int(entry.get())
    if num < 2:
        label_result.config(text="N is not prime")
        return
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            label_result.config(text="N is not prime")
            return
    label_result.config(text="N is prime")

def checkPerfect():
    num = int(entry.get())
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if num == sum:
        label_result.config(text="N is a perfect number")
    else: 
        label_result.config(text="N is not a perfect number")

def checkArmstrong():
    num = int(entry.get())
    sum = 0
    n = num
    while n > 0:
        r = n % 10
        sum += r ** 3
        n //= 10
    if num == sum:
        label_result.config(text="N is an Armstrong number")
    else: 
        label_result.config(text="N is not an Armstrong number")

root = tk.Tk()

label_prompt = tk.Label(root, text="Enter N")
label_prompt.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

selectedOp = tk.StringVar(value="prime")

primeBtn = tk.Radiobutton(root, text="Check Prime Number", value="prime", variable=selectedOp, command=checkPrime)
primeBtn.pack()

perfectBtn = tk.Radiobutton(root, text="Check Perfect Number", value="perfect", variable=selectedOp, command=checkPerfect)
perfectBtn.pack()

armstrongBtn = tk.Radiobutton(root, text="Check Armstrong Number", value="armstrong", variable=selectedOp, command=checkArmstrong)
armstrongBtn.pack()

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

root.mainloop()
