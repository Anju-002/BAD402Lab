# Python Program for 8 Queens Problem using Backtracking

N = 8

# Function to print the solution
def print_solution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

# Function to check if queen can be placed
def is_safe(board, row, col):

    # Check left side of row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

# Function to solve 8 Queens Problem
def solve_queen(board, col):

    # All queens are placed
    if col >= N:
        return True

    # Try placing queen in all rows
    for i in range(N):

        if is_safe(board, i, col):

            board[i][col] = 1

            if solve_queen(board, col + 1):
                return True

            # Backtrack
            board[i][col] = 0

    return False

# Driver Code
board = [[0 for x in range(N)] for y in range(N)]

if solve_queen(board, 0):
    print("Solution Found:\n")
    print_solution(board)
else:
    print("No Solution Exists")
