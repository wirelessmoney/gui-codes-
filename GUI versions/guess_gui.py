import tkinter as tk
import random

# Function to check the guess
def check_guess():
    try:
        guess = int(entry.get())
        if guess < target_number:
            result_label.config(text="Too low! Try again.")
        elif guess > target_number:
            result_label.config(text="Too high! Try again.")
        else:
            result_label.config(text="Correct! Well done.")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Generate a random number between 1 and 100
target_number = random.randint(1, 100)

# Setting up the main window
root = tk.Tk()
root.title("Guess the Number")
root.geometry("400x300")

# Label for instructions
instruction_label = tk.Label(root, text="Guess the number between 1 and 100", font=("Helvetica", 14))
instruction_label.pack(pady=10)

# Entry field for player's guess
entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack(pady=10)

# Button to check the guess
check_button = tk.Button(root, text="Check Guess", font=("Helvetica", 14), command=check_guess)
check_button.pack(pady=10)

# Label to display results
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

# Run the game
root.mainloop()
