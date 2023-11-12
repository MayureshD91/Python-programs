import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")

# Set up variables
current_player = "X"
board = [['' for _ in range(3)] for _ in range(3)]

# Function to handle the button click
def on_click(row, col):
    global current_player

    if board[row][col] == '':
        board[row][col] = current_player
        button_grid[row][col].config(text=current_player)

        # Check for a winner
        if check_winner():
            show_winner(current_player)
            return

        # Check for a draw
        if check_draw():
            show_draw()
            return

        # Switch to the other player
        current_player = "X" if current_player == "O" else "O"

# Function to check for a winner
def check_winner():
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return True
        if board[0][i] == board[1][i] == board[2][i] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

# Function to check for a draw
def check_draw():
    return all(all(cell != '' for cell in row) for row in board)

# Function to display the winner
def show_winner(player):
    messagebox.showinfo("Winner", f"Player {player} wins!")

# Function to display a draw message
def show_draw():
    messagebox.showinfo("Draw", "It's a draw!")

# Create buttons
button_grid = []
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = tk.Button(root, width=10, height=4, command=lambda row=i, col=j: on_click(row, col))
        button.grid(row=i, column=j)
        row_buttons.append(button)
    button_grid.append(row_buttons)

root.mainloop()