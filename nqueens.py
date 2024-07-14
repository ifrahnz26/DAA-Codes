'''Design and implement N-queens algorithm 
that displays the possible solutions on 4 x 4 chessboard. 
State the design strategy used and time complexity of the same.

'''

def placeQueens(board, row, N, solutions):
    if row == N:
        solutions.append(board[:])
        return True
    
    res = False
    for col in range(N):
        if isSafe(board, row, col):
            board[row] = col
            res = placeQueens(board, row + 1, N, solutions) or res
            board[row] = -1
    
    return res

def isSafe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True


N = int(input("Enter the size of the board: "))
board = [-1] * N
solutions = []
placeQueens(board, 0, N, solutions)

for idx, solution in enumerate(solutions, start=1):
    solution_1_indexed = [pos + 1 for pos in solution]
    print(f"Solution {idx}: {solution_1_indexed}")


