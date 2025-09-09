import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")

        self.choices = ["Rock", "Paper", "Scissors"]

        self.label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
        self.label.pack(pady=10)

        self.rock_button = tk.Button(root, text="Rock", font=("Arial", 14), width=10, command=lambda: self.play("Rock"))
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(root, text="Paper", font=("Arial", 14), width=10, command=lambda: self.play("Paper"))
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(root, text="Scissors", font=("Arial", 14), width=10, command=lambda: self.play("Scissors"))
        self.scissors_button.pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        result = self.get_result(user_choice, computer_choice)
        
        self.result_label.config(text=f"Computer chose {computer_choice}\n{result}")

    def get_result(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            return "You win!"
        else:
            return "You lose!"

def main():
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()

if __name__ == "__main__":
    main()
