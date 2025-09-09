import tkinter as tk
import time

# Function to start the timer
def start_timer():
    global start_time
    start_time = time.time()
    countdown()

# Function to update the countdown
def countdown():
    global start_time
    elapsed_time = time.time() - start_time
    time_left = max(0, 10 - int(elapsed_time))
    time_label.config(text=f"Time Left: {time_left}s")
    if time_left > 0:
        root.after(1000, countdown)  # Update every second
    else:
        result_label.config(text="Time's up! Try again!")

# Function to check if the button was pressed within time limit
def button_click():
    global start_time
    elapsed_time = time.time() - start_time
    if elapsed_time <= 10:
        result_label.config(text="You clicked on time!")
    else:
        result_label.config(text="You were too late!")

# Setting up the main window
root = tk.Tk()
root.title("Timer Game")
root.geometry("400x300")

# Label to show time remaining
time_label = tk.Label(root, text="Time Left: 10s", font=("Helvetica", 14))
time_label.pack(pady=20)

# Button to click
click_button = tk.Button(root, text="Click Me!", font=("Helvetica", 14), command=button_click)
click_button.pack(pady=20)

# Label to show result
result_label = tk.Label(root, text="Press the button before time runs out!", font=("Helvetica", 14))
result_label.pack(pady=20)

# Button to start the timer
start_button = tk.Button(root, text="Start Timer", font=("Helvetica", 14), command=start_timer)
start_button.pack(pady=20)

# Run the game
root.mainloop()
