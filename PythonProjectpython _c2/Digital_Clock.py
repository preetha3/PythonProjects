import tkinter as tk
from time import strftime

root = tk.Tk()
root.title('Digital Clock')

def time():
    string = strftime("%A::%I:%M:%S %p\n%D")
    label.config(text=string)
    label.after(1000, time)



label = tk.Label(root , font=("calibri",30), fg="black", bg="white")
label.pack(anchor="center")

time()
root.mainloop()
