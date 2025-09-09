import tkinter as tk
import time
import math

class AnimatedTextHeartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("I Love You with Heart Animation")
        self.root.geometry("600x400")

        # Create a canvas for drawing and animations
        self.canvas = tk.Canvas(root, width=600, height=400, bg="black")
        self.canvas.pack(fill="both", expand=True)

        # Create and animate text "I LOVE YOU"
        self.text = self.canvas.create_text(300, 100, text="I LOVE YOU", font=("Arial", 30), fill="white")
        self.animate_text()

        # Create and animate heart shape
        self.heart_points = self.generate_heart()
        self.heart = self.canvas.create_polygon(self.heart_points, fill="red", outline="")
        self.animate_heart()

    def generate_heart(self):
        # Define heart shape points
        heart_points = []
        for t in range(0, 360, 1):  # Generates points for heart
            rad = math.radians(t)
            x = 16 * math.sin(rad) ** 3
            y = 13 * math.cos(rad) - 5 * math.cos(2 * rad) - 2 * math.cos(3 * rad) - math.cos(4 * rad)
            heart_points.extend((300 + x * 30, 200 + y * 30))  # Scale the heart shape
        return heart_points

    def animate_text(self):
        x, y = self.canvas.coords(self.text)
        new_y = y + 2  # Animate text downward
        self.canvas.coords(self.text, x, new_y)
        if new_y < 300:
            self.root.after(30, self.animate_text)  # Continue animation

    def animate_heart(self):
        for i in range(0, len(self.heart_points), 2):
            x, y = self.heart_points[i], self.heart_points[i + 1]
            y += 1  # Animate heart upward
            self.heart_points[i + 1] = y
        self.canvas.coords(self.heart, *self.heart_points)  # Update heart position
        if self.heart_points[1] > 100:  # Continue animation while the heart is on the canvas
            self.root.after(30, self.animate_heart)

# Create the Tkinter window and run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = AnimatedTextHeartApp(root)
    root.mainloop()
