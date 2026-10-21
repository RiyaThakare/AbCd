N = int(input("Enter number of queens: "))
board = [-1] * N

def safe(row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve(col):
    if col == N:
        return True

    for row in range(N):
        if safe(row, col):
            board[col] = row

            if solve(col + 1):
                return True

            board[col] = -1

    return False

if solve(0):
    for row in range(N):
        for col in range(N):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution exists")
