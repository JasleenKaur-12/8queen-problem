def print_solution(board):
    """Print the board configuration."""
    for row in board:
        print(" ".join("Q" if x else "." for x in row))

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check the upper-left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check the upper-right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board), 1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(board, row):
    """Solve the N-Queens problem using backtracking."""
    n = len(board)
    
    # If all queens are placed, return True
    if row >= n:
        return True
    
    # Try placing the queen in all columns of the current row
    for col in range(n):
        if is_safe(board, row, col):
            # Place the queen
            board[row][col] = 1
            
            # Recursively place queens in the next row
            if solve_nqueens(board, row + 1):
                return True
            
            # If placing queen in board[row][col] doesn't lead to a solution,
            # backtrack: remove the queen
            board[row][col] = 0
    
    # If no column is found for the current row, return False
    return False

def solve_8queens():
    """Solve the 8 Queens problem."""
    n = 8  # Size of the chessboard (8x8)
    board = [[0 for _ in range(n)] for _ in range(n)]  # Initialize the chessboard
    
    if solve_nqueens(board, 0):
        print_solution(board)
    else:
        print("Solution does not exist")

# Run the solution
solve_8queens()
