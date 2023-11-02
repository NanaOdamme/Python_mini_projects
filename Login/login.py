#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox

def on_login_hover(event):
    login_button.config(bg="#0066cc")  # Change button color on hover

def on_login_leave(event):
    login_button.config(bg="#003399")  # Restore original button color

def login():
    username = entry1.get()
    password = entry2.get()

    if username == "" or password == "":
        messagebox.showinfo("", "Please enter both username and password.")
    elif username == "Admin" and password == "admin":
        messagebox.showinfo("", "Login successful")
    else:
        messagebox.showinfo("", "Incorrect username or password")

root = Tk()
root.title("Login")
root.geometry("500x450")  # window size
root.configure(bg="#87CEFA")  # background color

# Create a frame for the login form
frame = Frame(root, padx=20, pady=20, bg="#87CEFA")
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Username Label and Entry
username_label = Label(frame, text="Username", bg="#87CEFA", fg="white", font=("Arial", 14))
username_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry1 = Entry(frame, bd=8, width=30, font=("Arial", 16))
entry1.grid(row=1, column=0, padx=5, pady=5)

# Password Label and Entry
password_label = Label(frame, text="Password", bg="#87CEFA", fg="white", font=("Arial", 14))
password_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry2 = Entry(frame, show="*", bd=8, width=30, font=("Arial", 16))
entry2.grid(row=3, column=0, padx=5, pady=5)

# Login Button
login_button = Button(root, text="Login", command=login, height=2, width=18, bd=8, bg="#003399", fg="white")
login_button.pack(side="bottom", pady=10)

# Button hover effect
login_button.bind("<Enter>", on_login_hover)
login_button.bind("<Leave>", on_login_leave)

root.mainloop()
