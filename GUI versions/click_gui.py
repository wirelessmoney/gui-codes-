import tkinter as tk
import time


class ClickCounterGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Click Counter Game")
        
        self.clicks = 0
        self.time_left = 10
        self.running = False
        
        self.label = tk.Label(root, text="Click the button as many times as you can in 10 seconds!", font=("Arial", 14))
        self.label.pack(pady=10)

        self.click_button = tk.Button(root, text="Click Me!", font=("Arial", 14), width=10, command=self.count_click)
        self.click_button.pack(pady=10)

        self.time_label = tk.Label(root, text=f"Time left: {self.time_left} seconds", font=("Arial", 14))
        self.time_label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start", font=("Arial", 14), width=10, command=self.start_game)
        self.start_button.pack(pady=10)

    def count_click(self):
        if self.running:
            self.clicks += 1

    def start_game(self):
        if not self.running:
            self.running = True
            self.clicks = 0
            self.time_left = 10
            self.update_time()
            self.start_button.config(state="disabled")

    def update_time(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text=f"Time left: {self.time_left} seconds")
            self.root.after(1000, self.update_time)
        else:
            self.running = False
            messagebox.showinfo("Game Over", f"Time's up! You clicked {self.clicks} times.")
            self.start_button.config(state="normal")

def main():
    root = tk.Tk()
    game = ClickCounterGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
