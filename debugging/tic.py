def print_board(board):
    """
    Function Description:
    Prints the tic-tac-toe board.

    Parameters:
    board (list of lists): The 3x3 grid representing the tic-tac-toe board.

    Returns:
    None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Function Description:
    Checks if there is a winner on the tic-tac-toe board.

    Parameters:
    board (list of lists): The 3x3 grid representing the tic-tac-toe board.

    Returns:
    bool: True if there is a winner, False otherwise.
    """
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False
    
def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":
                    board[row][col] = player
                    if check_winner(board):
                        break
                    player = "X" if player == "O" else "O"
                else:
                    print("That spot is already taken! Try again.")
            else:
                print("Invalid input. Please enter a number between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print_board(board)
    if check_winner(board):
        print("Player " + player + " wins!")
    else:
        print("It's a draw!")

tic_tac_toe()
