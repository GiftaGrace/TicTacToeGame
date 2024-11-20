def print_board(board):
    # Function to print the Tic-Tac-Toe board
    print("\n")
    for row in range(3):
        print(" | ".join(board[row]))
        if row < 2:
            print("---------")
    print("\n")

def check_winner(board, player):
    # Check rows, columns, and diagonals for a winner
    for row in range(3):
        if all([cell == player for cell in board[row]]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    
    # Initialize empty 3x3 board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    # Set the starting player
    current_player = 'X'
    
    # Play the game
    for turn in range(9):
        print_board(board)
        print(f"Player {current_player}'s turn:")
        
        # Get the player's move
        while True:
            try:
                row, col = map(int, input("Enter row and column (0-2) separated by a space: ").split())
                if board[row][col] == ' ':
                    board[row][col] = current_player
                    break
                else:
                    print("That spot is already taken. Choose a different one.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column numbers between 0 and 2.")
        
        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'
    
    else:
        print_board(board)
        print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
