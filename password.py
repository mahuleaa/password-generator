import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from random import choice, randint
import string

def generate_password():
    length = length_slider.get()

    if length < 4:
        messagebox.showwarning("Invalid Length", "Password length should be at least 4 characters.")
        return

    password = ""
    characters = string.ascii_letters + string.digits + string.punctuation

    for _ in range(length):
        password += choice(characters)

    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Password Copied", "Password copied to clipboard.")

def main():
    global root, length_slider, password_entry, username_entry

    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("400x400")
    root.resizable(False, False)

    # Create a themed style
    style = ttk.Style()
    style.theme_use("clam")  # Choose from 'clam', 'alt', 'default', 'classic'

    # Change background and foreground colors
    style.configure("TLabel", background="#EFEFEF", foreground="#333333")
    style.configure("TEntry", fieldbackground="white")
    style.configure("TButton", background="#4C4C4C", foreground="white")

    heading_label = ttk.Label(
        root,
        text="Password Generator",
        font=("Arial", 24, "bold"),
    )
    heading_label.pack(padx=10, pady=20)

    username_label = ttk.Label(
        root,
        text="Username:",
        font=("Arial", 14),
    )
    username_label.pack(pady=5)

    username_entry = ttk.Entry(
        root,
        font=("Arial", 14),
        width=30
    )
    username_entry.pack(pady=5)

    length_label = ttk.Label(
        root,
        text="Password Length:",
        font=("Arial", 14),
    )
    length_label.pack(pady=5)

    length_slider = ttk.Scale(
        root,
        from_=4,
        to=32,
        orient=tk.HORIZONTAL,
        length=200,
    )
    length_slider.set(8)
    length_slider.pack()

    generate_button = ttk.Button(
        root,
        text="Generate Password",
        command=generate_password
    )
    generate_button.pack(pady=15)

    password_entry = ttk.Entry(
        root,
        font=("Courier New", 14),
        width=30
    )
    password_entry.pack(pady=15)

    copy_button = ttk.Button(
        root,
        text="Copy Password",
        command=copy_password
    )
    copy_button.pack(pady=15)

    root.mainloop()

if __name__ == "__main__":
    main()
