import tkinter as tk
import math

# Main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x550")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief=tk.RIDGE, justify="right")
entry.pack(fill="both", padx=10, pady=10, ipady=10)

# Functions
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def scientific(func):
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)

        if func == "sin":
            entry.insert(tk.END, math.sin(math.radians(value)))
        elif func == "cos":
            entry.insert(tk.END, math.cos(math.radians(value)))
        elif func == "tan":
            entry.insert(tk.END, math.tan(math.radians(value)))
        elif func == "sqrt":
            entry.insert(tk.END, math.sqrt(value))
        elif func == "log":
            entry.insert(tk.END, math.log10(value))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Buttons
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")
    for btn in row:
        action = lambda x=btn: calculate() if x == '=' else click(x)
        tk.Button(
            row_frame,
            text=btn,
            font=("Arial", 16),
            command=action
        ).pack(side="left", expand=True, fill="both")

# Scientific buttons
sci_frame = tk.Frame(root)
sci_frame.pack(expand=True, fill="both")

tk.Button(sci_frame, text="SIN", font=("Arial", 14), command=lambda: scientific("sin")).pack(side="left", expand=True, fill="both")
tk.Button(sci_frame, text="COS", font=("Arial", 14), command=lambda: scientific("cos")).pack(side="left", expand=True, fill="both")
tk.Button(sci_frame, text="TAN", font=("Arial", 14), command=lambda: scientific("tan")).pack(side="left", expand=True, fill="both")
tk.Button(sci_frame, text="√", font=("Arial", 14), command=lambda: scientific("sqrt")).pack(side="left", expand=True, fill="both")
tk.Button(sci_frame, text="LOG", font=("Arial", 14), command=lambda: scientific("log")).pack(side="left", expand=True, fill="both")

# Clear button
tk.Button(root, text="CLEAR", font=("Arial", 16), bg="red", fg="white", command=clear).pack(fill="both", padx=10, pady=10)

root.mainloop()
