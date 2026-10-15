import tkinter as tk
from tkinter import messagebox


def submit_form():
    user_name = user_name_entry.get()
    password = password_entry.get()

    if not user_name or not password:
        messagebox.showwarning("Missing Details", "Please enter User Name/ID and Password.")
        return

    messagebox.showinfo("Submitted", f"User Name/ID: {user_name}")


def reset_form():
    user_name_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    user_name_entry.focus()


window = tk.Tk()
window.title("Login Window")
window.geometry("350x220")
window.resizable(False, False)

title_label = tk.Label(window, text="Login Details", font=("Arial", 16, "bold"))
title_label.pack(pady=15)

form_frame = tk.Frame(window)
form_frame.pack(pady=5)

user_name_label = tk.Label(form_frame, text="User Name/ID:", font=("Arial", 11))
user_name_label.grid(row=0, column=0, padx=10, pady=8, sticky="e")

user_name_entry = tk.Entry(form_frame, width=25)
user_name_entry.grid(row=0, column=1, padx=10, pady=8)

password_label = tk.Label(form_frame, text="Password:", font=("Arial", 11))
password_label.grid(row=1, column=0, padx=10, pady=8, sticky="e")

password_entry = tk.Entry(form_frame, width=25, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=8)

button_frame = tk.Frame(window)
button_frame.pack(pady=18)

submit_button = tk.Button(button_frame, text="Submit", width=10, command=submit_form)
submit_button.grid(row=0, column=0, padx=10)

reset_button = tk.Button(button_frame, text="Reset", width=10, command=reset_form)
reset_button.grid(row=0, column=1, padx=10)

user_name_entry.focus()
window.mainloop()
