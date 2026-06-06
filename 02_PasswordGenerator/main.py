import tkinter as tk
from tkinter import messagebox
import random
import string

# -----------------------------
# Generate Password Function
# -----------------------------
def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showwarning(
                "Warning",
                "Password length should be at least 4!"
            )
            return

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = "".join(random.choice(characters) for _ in range(length))

        password_var.set(password)

        # Password Strength
        if length < 8:
            strength_label.config(text="Strength: Weak")
        elif length < 12:
            strength_label.config(text="Strength: Medium")
        else:
            strength_label.config(text="Strength: Strong")

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter a valid number."
        )


# -----------------------------
# Copy Password
# -----------------------------
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard!"
    )


# -----------------------------
# Show / Hide Password
# -----------------------------
def toggle_password():
    if result_entry.cget("show") == "*":
        result_entry.config(show="")
        show_btn.config(text="Hide")
    else:
        result_entry.config(show="*")
        show_btn.config(text="Show")


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()

root.title("Password Generator")
root.geometry("550x420")
root.resizable(False, False)
root.configure(bg="#1E1E2F")


# -----------------------------
# Title
# -----------------------------
title = tk.Label(
    root,
    text="🔐 Password Generator",
    font=("Helvetica", 22, "bold"),
    bg="#1E1E2F",
    fg="white"
)

title.pack(pady=20)


# -----------------------------
# Length Label
# -----------------------------
length_label = tk.Label(
    root,
    text="Enter Password Length",
    font=("Arial", 12),
    bg="#1E1E2F",
    fg="white"
)

length_label.pack()

length_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center",
    width=15
)

length_entry.pack(pady=10)


# -----------------------------
# Generate Button
# -----------------------------
generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    width=22,
    command=generate_password,
    bg="#4CAF50",
    fg="white"
)

generate_btn.pack(pady=10)


# -----------------------------
# Password Display
# -----------------------------
password_var = tk.StringVar()

result_entry = tk.Entry(
    root,
    textvariable=password_var,
    font=("Consolas", 14),
    width=30,
    justify="center",
    show="*"
)

result_entry.pack(pady=10)


# -----------------------------
# Show Button
# -----------------------------
show_btn = tk.Button(
    root,
    text="Show",
    font=("Arial", 11),
    width=10,
    command=toggle_password,
    bg="#2196F3",
    fg="white"
)

show_btn.pack(pady=5)


# -----------------------------
# Copy Button
# -----------------------------
copy_btn = tk.Button(
    root,
    text="📋 Copy Password",
    font=("Arial", 12, "bold"),
    width=22,
    command=copy_password,
    bg="#FF9800",
    fg="white"
)

copy_btn.pack(pady=10)


# -----------------------------
# Strength Label
# -----------------------------
strength_label = tk.Label(
    root,
    text="Strength: -",
    font=("Arial", 12, "bold"),
    bg="#1E1E2F",
    fg="white"
)

strength_label.pack(pady=15)


# -----------------------------
# Run App
# -----------------------------
root.mainloop()