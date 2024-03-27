import numpy as np

sudoku = [[0,8,9,0,6,0,0,0,0],
          [0,0,0,5,0,0,0,0,8],
          [6,1,0,0,0,0,9,3,0],
          [0,0,0,4,3,0,0,7,9],
          [1,0,0,0,9,0,0,0,0],
          [0,0,4,6,0,0,8,5,0],
          [3,0,0,0,5,7,0,0,0],
          [0,9,7,0,4,6,5,2,3],
          [5,4,1,0,2,8,0,9,6]]

def print_board(board):
    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(board[0])):
            if j%3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def possible(board, pos, n):
    for i in range(0, 9):
        if board[pos[0]][i] == n:
            return False
    for j in range(0, 9):
        if board[j][pos[1]] == n:
            return False

    x0 = (pos[0] // 3)*3
    y0 = (pos[1] // 3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[x0 + i][y0 + j] == n:
                return False
    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if possible(board, (row, col), i):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

print(print_board(sudoku))
solve(sudoku)
print("\t")
print(print_board(sudoku))