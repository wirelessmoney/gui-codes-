import tkinter as tk
from tkinter import messagebox

# Starting balance
balance = 50000.0

# Function to show the current balance
def show_balance():
    balance_label.config(text=f"Current Balance: ${balance:.2f}")

# Function to deposit money
def deposit():
    global balance  # Declare balance as global to modify it
    try:
        amount = float(deposit_entry.get())
        if amount <= 0:
            messagebox.showerror("Invalid Amount", "Deposit amount must be positive!")
        else:
            balance += amount
            show_balance()
            deposit_entry.delete(0, tk.END)
            messagebox.showinfo("Deposit", f"Successfully deposited ${amount:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount to deposit.")

# Function to withdraw money
def withdraw():
    global balance  # Declare balance as global to modify it
    try:
        amount = float(withdraw_entry.get())
        if amount <= 0:
            messagebox.showerror("Invalid Amount", "Withdrawal amount must be positive!")
        elif amount > balance:
            messagebox.showerror("Insufficient Funds", "You do not have enough balance to withdraw that amount.")
        else:
            balance -= amount
            show_balance()
            withdraw_entry.delete(0, tk.END)
            messagebox.showinfo("Withdrawal", f"Successfully withdrew ${amount:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount to withdraw.")

# Setting up the main window
root = tk.Tk()
root.title("ATM System")
root.geometry("400x400")

# Label for displaying balance
balance_label = tk.Label(root, text=f"Current Balance: ${balance:.2f}", font=("Helvetica", 16))
balance_label.pack(pady=20)

# Deposit Section
deposit_frame = tk.Frame(root)
deposit_frame.pack(pady=10)
deposit_label = tk.Label(deposit_frame, text="Deposit Amount:", font=("Helvetica", 12))
deposit_label.pack(side=tk.LEFT)
deposit_entry = tk.Entry(deposit_frame, font=("Helvetica", 12))
deposit_entry.pack(side=tk.LEFT)
deposit_button = tk.Button(deposit_frame, text="Deposit", font=("Helvetica", 12), command=deposit)
deposit_button.pack(side=tk.LEFT)

# Withdraw Section
withdraw_frame = tk.Frame(root)
withdraw_frame.pack(pady=10)
withdraw_label = tk.Label(withdraw_frame, text="Withdraw Amount:", font=("Helvetica", 12))
withdraw_label.pack(side=tk.LEFT)
withdraw_entry = tk.Entry(withdraw_frame, font=("Helvetica", 12))
withdraw_entry.pack(side=tk.LEFT)
withdraw_button = tk.Button(withdraw_frame, text="Withdraw", font=("Helvetica", 12), command=withdraw)
withdraw_button.pack(side=tk.LEFT)

# Show current balance button
show_balance_button = tk.Button(root, text="Show Balance", font=("Helvetica", 12), command=show_balance)
show_balance_button.pack(pady=20)

# Run the main event loop
root.mainloop()
