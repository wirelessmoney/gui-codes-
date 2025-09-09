import tkinter as tk

# Function to handle button clicks
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Setting up the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")

# Entry field to display the current input
entry = tk.Entry(root, font=("Helvetica", 18), borderwidth=2, relief="solid", width=16, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button definitions
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, font=("Helvetica", 18), command=evaluate_expression, width=5)
    elif text == "C":
        button = tk.Button(root, text=text, font=("Helvetica", 18), command=clear_entry, width=5)
    else:
        button = tk.Button(root, text=text, font=("Helvetica", 18), command=lambda value=text: button_click(value), width=5)
    
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the main event loop
root.mainloop()
