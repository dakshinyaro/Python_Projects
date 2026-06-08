import tkinter as tk

# Functions
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Main Window
root = tk.Tk()
root.title("Colorful Calculator")
root.geometry("400x500")
root.configure(bg="#1E1E2F")
root.resizable(False, False)

# Display
entry = tk.Entry(
    root,
    font=("Arial", 24),
    bd=10,
    relief=tk.RIDGE,
    justify="right",
    bg="#F8F8F8"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

# Button Styling
btn_font = ("Arial", 14, "bold")

buttons = [
    ('7', 1, 0, "#4CAF50"),
    ('8', 1, 1, "#4CAF50"),
    ('9', 1, 2, "#4CAF50"),
    ('/', 1, 3, "#FF9800"),

    ('4', 2, 0, "#4CAF50"),
    ('5', 2, 1, "#4CAF50"),
    ('6', 2, 2, "#4CAF50"),
    ('*', 2, 3, "#FF9800"),

    ('1', 3, 0, "#4CAF50"),
    ('2', 3, 1, "#4CAF50"),
    ('3', 3, 2, "#4CAF50"),
    ('-', 3, 3, "#FF9800"),

    ('0', 4, 0, "#4CAF50"),
    ('.', 4, 1, "#4CAF50"),
    ('=', 4, 2, "#2196F3"),
    ('+', 4, 3, "#FF9800"),
]

for (text, row, col, color) in buttons:
    if text == "=":
        button = tk.Button(
            root,
            text=text,
            font=btn_font,
            bg=color,
            fg="white",
            width=6,
            height=2,
            command=calculate
        )
    else:
        button = tk.Button(
            root,
            text=text,
            font=btn_font,
            bg=color,
            fg="white",
            width=6,
            height=2,
            command=lambda t=text: click(t)
        )

    button.grid(row=row, column=col, padx=5, pady=5)

# Clear Button
clear_btn = tk.Button(
    root,
    text="CLEAR",
    font=("Arial", 14, "bold"),
    bg="#F44336",
    fg="white",
    width=28,
    height=2,
    command=clear
)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

root.mainloop()