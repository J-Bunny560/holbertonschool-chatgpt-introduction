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
    """
    Function Description:
    Runs the tic-tac-toe game.

    Parameters:
    None

    Returns:
    None
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                raise ValueError("Row and column indices must be 0, 1, or 2.")
            if board[row][col] == " ":
                board[row][col] = player
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError as e:
            print("Invalid input:", e)

    print_board(board)
    print("Player " + player + " wins!")

tic_tac_toe()
