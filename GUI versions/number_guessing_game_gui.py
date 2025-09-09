import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        
        self.label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.button = tk.Button(root, text="Submit Guess", font=("Arial", 14), command=self.check_guess)
        self.button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            if guess < self.number_to_guess:
                self.result_label.config(text="Too low! Try again.", fg="blue")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Too high! Try again.", fg="blue")
            else:
                messagebox.showinfo("You Win!", f"Correct! You guessed the number in {self.attempts} attempts.")
                self.reset_game()
        except ValueError:
            self.result_label.config(text="Please enter a valid number.", fg="red")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

def main():
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
