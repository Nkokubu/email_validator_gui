import re
import tkinter as tk
from tkinter import messagebox

def is_valid_email(email):
    # Simple regex for email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_email():
    email = entry.get()
    if is_valid_email(email):
        result_label.config(text="✅ Valid Email", fg="green")
    else:
        result_label.config(text="❌ Invalid Email", fg="red")

# Set up GUI window
root = tk.Tk()
root.title("Email Validator")
root.geometry("400x150")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Enter your email address:").pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack()

tk.Button(root, text="Validate", command=validate_email).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Run the app
root.mainloop()
