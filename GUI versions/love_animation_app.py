import tkinter as tk
import random
import math

class LoveAnimationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("I Love You, mi amour")
        self.root.geometry("600x400")

        # Create a canvas for the animation
        self.canvas = tk.Canvas(root, width=600, height=400, bg="black")
        self.canvas.pack(fill="both", expand=True)

        # Display the text
        self.text = self.canvas.create_text(300, 50, text="I LOVE YOU, MI AMOUR", font=("Arial", 24, "bold"), fill="white")

        # Create shapes (hearts and circles)
        self.shapes = []
        for _ in range(10):  # Create 10 shapes
            x = random.randint(50, 550)
            y = random.randint(100, 350)
            dx = random.uniform(-2, 2)
            dy = random.uniform(-2, 2)
            if random.choice([True, False]):
                shape = self.create_heart(x, y, size=random.randint(20, 30))
            else:
                shape = self.canvas.create_oval(x, y, x + 30, y + 30, fill="red", outline="")
            self.shapes.append((shape, dx, dy))

        # Start the animation
        self.animate_shapes()

    def create_heart(self, x, y, size=20):
        """Create a heart shape at (x, y)."""
        points = []
        for angle in range(0, 360, 1):
            rad = math.radians(angle)
            x_offset = 16 * math.sin(rad)**3
            y_offset = 13 * math.cos(rad) - 5 * math.cos(2 * rad) - 2 * math.cos(3 * rad) - math.cos(4 * rad)
            points.append((x + x_offset * size / 30, y - y_offset * size / 30))
        return self.canvas.create_polygon(points, fill="pink", outline="")

    def animate_shapes(self):
        """Animate shapes on the canvas."""
        for i, (shape, dx, dy) in enumerate(self.shapes):
            # Move the shape
            self.canvas.move(shape, dx, dy)

            # Get the current position
            coords = self.canvas.coords(shape)
            x1, y1, x2, y2 = coords if len(coords) == 4 else (coords[0], coords[1], coords[0] + 30, coords[1] + 30)

            # Bounce off the walls
            if x1 <= 0 or x2 >= 600:
                dx = -dx
            if y1 <= 0 or y2 >= 400:
                dy = -dy

            # Update the shape's movement
            self.shapes[i] = (shape, dx, dy)

        # Schedule the next frame
        self.root.after(30, self.animate_shapes)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = LoveAnimationApp(root)
    root.mainloop()

