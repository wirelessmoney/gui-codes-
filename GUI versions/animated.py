import tkinter as tk
import random

class AnimatedBackgroundApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Animated Background with GUI")
        self.root.geometry("600x400")

        # Create a canvas for the animated background
        self.canvas = tk.Canvas(root, width=600, height=400, bg="black")
        self.canvas.pack(fill="both", expand=True)

        # Add some animated shapes
        self.shapes = []
        for _ in range(10):
            x1 = random.randint(0, 580)
            y1 = random.randint(0, 380)
            x2 = x1 + random.randint(20, 50)
            y2 = y1 + random.randint(20, 50)
            color = random.choice(["red", "green", "blue", "yellow", "purple", "orange"])
            shape = self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline="")
            dx = random.choice([-2, -1, 1, 2])  # Random x-direction speed
            dy = random.choice([-2, -1, 1, 2])  # Random y-direction speed
            self.shapes.append((shape, dx, dy))

        # Add GUI elements
        self.label = tk.Label(root, text="Welcome to the Animated GUI!", font=("Arial", 14), bg="black", fg="white")
        self.label.place(x=150, y=10)

        self.button = tk.Button(root, text="Click Me", command=self.button_clicked)
        self.button.place(x=260, y=50)

        # Start the animation loop
        self.animate()

    def animate(self):
        for i, (shape, dx, dy) in enumerate(self.shapes):
            self.canvas.move(shape, dx, dy)
            x1, y1, x2, y2 = self.canvas.coords(shape)

            # Bounce shapes off the edges
            if x1 <= 0 or x2 >= 600:
                dx = -dx
            if y1 <= 0 or y2 >= 400:
                dy = -dy

            # Update the shape's movement
            self.shapes[i] = (shape, dx, dy)

        # Schedule the next frame
        self.root.after(30, self.animate)

    def button_clicked(self):
        self.label.config(text="Button Clicked!")

# Create the Tkinter window and run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = AnimatedBackgroundApp(root)
    root.mainloop()
