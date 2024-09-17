import tkinter as tk
import time
import random

def update_time():
    string = time.strftime('%H:%M:%S %p')
    label.config(text=string, fg = get_random_color())
    label.after(1000, update_time)

def get_random_color():
    color = "#{:06x}".format(random.randint(0,0xFFFFFF))
    return color

root = tk.Tk()
root.title("Clock")

label = tk.Label(root, font=("ds-digital", 80), bg = "black")
label.pack(anchor='center')
update_time()
root.mainloop()