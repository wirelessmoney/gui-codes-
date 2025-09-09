import tkinter as tk
import random
import time

# Function to start the game
def start_game():
    global start_time
    start_time = time.time()
    update_button_position()

# Function to update the button's position to a random spot
def update_button_position():
    button.place(x=random.randint(0, 400), y=random.randint(0, 400))

# Function to handle button click
def button_click():
    global start_time
    end_time = time.time()
    elapsed_time = end_time - start_time
    score_label.config(text=f"Time: {elapsed_time:.2f} seconds")
    update_button_position()

# Setting up the main window
root = tk.Tk()
root.title("Click Game")
root.geometry("500x500")

# Label to show the score (time taken)
score_label = tk.Label(root, text="Click the button!", font=("Helvetica", 16))
score_label.pack(pady=20)

# Button that moves around and can be clicked
button = tk.Button(root, text="Click Me!", font=("Helvetica", 14), command=button_click)
button.place(x=200, y=200)

# Button to start the game
start_button = tk.Button(root, text="Start Game", font=("Helvetica", 14), command=start_game)
start_button.pack(pady=20)

# Run the game
root.mainloop()
