def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("---------")

def check_winner(board):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    return None

def minimax(board, is_max):
    winner = check_winner(board)

    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if " " not in board:
        return 0

    if is_max:
        best = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best = max(best, score)

        return best

    else:
        best = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best = min(best, score)

        return best

def best_move(board):
    best_score = -float("inf")
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move

board = [" "] * 9

print("Tic-Tac-Toe: You are X, Computer is O")

while True:
    print_board(board)

    # Human player's move
    pos = int(input("Enter position (1-9): ")) - 1

    if pos < 0 or pos > 8 or board[pos] != " ":
        print("Invalid move! Try again.")
        continue

    board[pos] = "X"

    if check_winner(board) == "X":
        print_board(board)
        print("You win!")
        break

    if " " not in board:
        print_board(board)
        print("Draw!")
        break

    # Computer's move using Minimax
    pos = best_move(board)
    board[pos] = "O"

    if check_winner(board) == "O":
        print_board(board)
        print("Computer wins!")
        break

    if " " not in board:
        print_board(board)
        print("Draw!")
        break
