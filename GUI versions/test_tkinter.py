import tkinter as tk

# Test Tkinter window
root = tk.Tk()
root.title("Tkinter Test")

label = tk.Label(root, text="Tkinter is working!")
label.pack()

root.mainloop()
