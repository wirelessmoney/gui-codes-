import tkinter as tk
import time

class AnimatedTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("I Love You, little lamb Animation")
        self.root.geometry("600x400")
        
        # Create a canvas for drawing the text
        self.canvas = tk.Canvas(root, width=600, height=400, bg="black")
        self.canvas.pack(fill="both", expand=True)
        
        # Coordinates for the text
        self.text_x = 300
        self.text_y = 100
        self.text_content = "I LOVE YOU, LITTLE LAMB"
        
        # Animate the text
        self.animate_text()
    
    def animate_text(self):
        # Clear the previous text
        self.canvas.delete("text")
        
        # Draw the current position of the text
        self.canvas.create_text(self.text_x, self.text_y, text=self.text_content, font=("Arial", 20), fill="white", tags="text")
        
        # Move the text downwards
        self.text_y += 1
        if self.text_y < 300:
            self.root.after(30, self.animate_text)  # Continue animation
        
# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = AnimatedTextApp(root)
    root.mainloop()
