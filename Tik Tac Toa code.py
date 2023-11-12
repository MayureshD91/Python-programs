# Function to display the Tic Tac Toe board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full (draw)
def check_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Function to get a valid move from the player
def get_move(board):
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                return row, col
            print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter valid row and column.")

# Main function to run the game
def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    player_idx = 0

    print("Welcome to Tic Tac Toe!")
    display_board(board)

    for _ in range(9):
        player = players[player_idx]
        print(f"Player {player}'s turn.")
        row, col = get_move(board)
        board[row][col] = player
        display_board(board)

        if check_winner(board, player):
            print(f"Player {player} wins!")
            break

        if check_draw(board):
            print("It's a draw!")
            break

        player_idx = 1 - player_idx

if __name__ == "__main__":
    main()