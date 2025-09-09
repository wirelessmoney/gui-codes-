import tkinter as tk
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        
        self.label = tk.Label(master, text="Guess a number between 1 and 100")
        self.label.pack()
        
        self.entry = tk.Entry(master)
        self.entry.pack()
        
        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()
        
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def check_guess(self):
        guess = int(self.entry.get())
        self.attempts += 1
        
        if guess < self.number_to_guess:
            self.result_label.config(text="Too low! Try again.")
        elif guess > self.number_to_guess:
            self.result_label.config(text="Too high! Try again.")
        else:
            self.result_label.config(text=f"Correct! You guessed it in {self.attempts} attempts.")
            self.number_to_guess = random.randint(1, 100)  # Reset the game for a new round

def main():
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()

main()
