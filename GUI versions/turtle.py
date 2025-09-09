import turtle
import random
import tkinter as tk
from tkinter import messagebox

def setup_race():
    screen.clear()
    screen.bgcolor("white")
    
    # Draw finish line
    finish_line = 200
    screen.tracer(0)
    drawer.penup()
    drawer.goto(finish_line, 150)
    drawer.pendown()
    drawer.goto(finish_line, -150)
    screen.tracer(1)
    
    # Create turtles
    colors = ["red", "blue", "green", "orange", "purple"]
    y_positions = [-100, -50, 0, 50, 100]
    
    for i in range(5):
        racer = turtle.Turtle()
        racer.color(colors[i])
        racer.shape("turtle")
        racer.penup()
        racer.goto(-200, y_positions[i])
        turtles.append(racer)

def start_race():
    while True:
        for racer in turtles:
            racer.forward(random.randint(1, 10))
            if racer.xcor() >= 200:
                winner = racer.color()[0]
                messagebox.showinfo("Race Over", f"The {winner} turtle wins!")
                return

# Initialize screen and turtle drawer
screen = turtle.Screen()
screen.title("Turtle Race Game")
screen.setup(width=500, height=400)
drawer = turtle.Turtle()
drawer.hideturtle()
turtles = []

# Tkinter GUI setup
root = tk.Tk()
root.title("Turtle Race Controller")
root.geometry("300x200")

setup_button = tk.Button(root, text="Setup Race", command=setup_race)
setup_button.pack(pady=10)

start_button = tk.Button(root, text="Start Race", command=start_race)
start_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

root.mainloop()
