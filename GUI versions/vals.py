import tkinter as tk
from tkinter import messagebox

def show_love_message():
    love_message = entry.get("1.0", tk.END).strip()
    print(f"Debug: Retrieved message - {love_message}")
    if love_message:
        messagebox.showinfo("Your Valentine's Message", love_message)
    else:
        messagebox.showwarning("Oops!", "Please enter a message before sending!")

# Create main window
root = tk.Tk()
root.title("Valentine's Letter")
root.geometry("400x300")
root.configure(bg='#ffcccc')

# Heading label
label = tk.Label(root, text="Write Your Valentine's Message", font=("Arial", 14, "bold"), bg='#ffcccc')
label.pack(pady=10)

#text box input 
entry = tk.Text(root, width=40, height=5, font=("Arial", 12))
entry.pack(pady=10)

#button to submit 
send_button = tk.Button(root, text="Send", command=show_love_message, font=("Arial", 12, "bold"), bg='#ff66b2', fg='white')
send_button.pack(pady=10)

#run the main event loop
root.mainloop()