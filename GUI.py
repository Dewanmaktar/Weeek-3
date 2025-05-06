import tkinter as tk
from tkinter import messagebox

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            input_var.set(result)
            expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            expression = ""
            input_var.set("")
    elif text == "C":
        expression = ""
        input_var.set("")
    else:
        expression += text
        input_var.set(expression)

# Initialize the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

expression = ""
input_var = tk.StringVar()

# Entry widget to display the current expression
entry = tk.Entry(root, textvar=input_var, font=("Arial", 20), justify="right", bd=8, relief=tk.SUNKEN)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack()

# Button layout
buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row = 0
col = 0
for button in buttons:
    btn = tk.Button(button_frame, text=button, font=("Arial", 18), relief=tk.RAISED, bd=4)
    btn.grid(row=row, column=col, padx=10, pady=10, ipadx=10, ipady=10)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the application
root.mainloop()