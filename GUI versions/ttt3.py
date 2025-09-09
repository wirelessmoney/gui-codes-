import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.current_player = "X"
        self.board = [""] * 9  # A list to represent the 3x3 grid
        self.buttons = []

        # Create the buttons for the Tic-Tac-Toe grid
        for i in range(9):
            button = tk.Button(root, text="", font=("normal", 20), width=10, height=3,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def make_move(self, index):
        # If the cell is already filled, do nothing
        if self.board[index] != "":
            return

        # Mark the cell with the current player's symbol (X or O)
        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player)

        # Check if the current player has won
        if self.check_winner(self.current_player):
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            self.reset_game()
            return

        # Check for a tie
        if "" not in self.board:
            messagebox.showinfo("Game Over", "It's a tie!")
            self.reset_game()
            return

        # Switch to the other player
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        # Check rows, columns, and diagonals for a win
        win_conditions = [
            [0, 1, 2],  # First row
            [3, 4, 5],  # Second row
            [6, 7, 8],  # Third row
            [0, 3, 6],  # First column
            [1, 4, 7],  # Second column
            [2, 5, 8],  # Third column
            [0, 4, 8],  # Diagonal from top-left to bottom-right
            [2, 4, 6]   # Diagonal from top-right to bottom-left
        ]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

    def reset_game(self):
        # Reset the board and buttons for a new game
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "X"

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
