import tkinter as tk
from tkinter import messagebox

# Questions
quiz_data = [
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Processing Unit",
            "Central Program Utility",
            "Computer Program Unit"
        ],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which language is used for Data Science?",
        "options": ["Python", "HTML", "CSS", "JavaScript"],
        "answer": "Python"
    },
    {
        "question": "Which company developed Windows?",
        "options": ["Apple", "Google", "Microsoft", "IBM"],
        "answer": "Microsoft"
    },
    {
        "question": "What does RAM stand for?",
        "options": [
            "Random Access Memory",
            "Read Access Memory",
            "Run Access Memory",
            "Rapid Access Memory"
        ],
        "answer": "Random Access Memory"
    },
    {
        "question": "Which protocol is used to browse websites?",
        "options": ["FTP", "SMTP", "HTTP", "SSH"],
        "answer": "HTTP"
    }
]

current_question = 0
score = 0

# Check answer
def check_answer():
    global current_question, score

    selected = option_var.get()

    if selected == quiz_data[current_question]["answer"]:
        score += 1

    current_question += 1

    if current_question < len(quiz_data):
        load_question()
    else:
        messagebox.showinfo(
            "Quiz Completed",
            f"Your Score: {score}/{len(quiz_data)}"
        )
        root.destroy()

# Load question
def load_question():
    question_label.config(
        text=quiz_data[current_question]["question"]
    )

    option_var.set(None)

    for i in range(4):
        options[i].config(
            text=quiz_data[current_question]["options"][i],
            value=quiz_data[current_question]["options"][i]
        )

# GUI Window
root = tk.Tk()
root.title("Quiz Application")
root.geometry("700x500")
root.configure(bg="#1E1E2F")

title = tk.Label(
    root,
    text="Quiz Application",
    font=("Arial", 22, "bold"),
    bg="#1E1E2F",
    fg="white"
)
title.pack(pady=20)

question_label = tk.Label(
    root,
    text="",
    font=("Arial", 16),
    wraplength=600,
    bg="#1E1E2F",
    fg="white"
)
question_label.pack(pady=20)

option_var = tk.StringVar()

options = []

for _ in range(4):
    rb = tk.Radiobutton(
        root,
        text="",
        variable=option_var,
        value="",
        font=("Arial", 14),
        bg="#1E1E2F",
        fg="white",
        selectcolor="#4CAF50",
        activebackground="#1E1E2F"
    )
    rb.pack(anchor="w", padx=100, pady=5)
    options.append(rb)

submit_btn = tk.Button(
    root,
    text="Next Question",
    font=("Arial", 14, "bold"),
    bg="#2196F3",
    fg="white",
    command=check_answer
)
submit_btn.pack(pady=30)

load_question()

root.mainloop()