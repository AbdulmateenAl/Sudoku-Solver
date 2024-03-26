import numpy as np

sudoku = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]
#print(np.matrix(sudoku))

def possible(x, y, n):
    global sudoku
    for i in range(0, 9):
        if sudoku[x][i] == n:
            return False
    for j in range(0, 9):
        if sudoku[i][y] == n:
            return False

    x0 = (x // 3)*3
    y0 = (y // 3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[y0 + i][x0 + j] == n:
                return False
    return True

# def automate():
#     global sudoku
#     for i in range(0,9):
#         for j in range(0,9):
#             if sudoku[i][j] == 0:
#                 for n in range(0, 10):
#                     if possible(i, j, n):
#                         sudoku[i][j] = n
#                         automate()
#                         sudoku[i][j] = 0
#                 return 
#     new = np.matrix(sudoku)
#     print(new)
#     input("More?")
def automate():
    global sudoku
    for i in range(0, 9):
        for j in range(0, 9):
            if i == 8 and j == 8:
                break
            elif sudoku[i][j] == 0:
                for n in range(0, 10):
                    if possible(i, j, n):
                        sudoku[i][j] == n
                        automate()
                    sudoku[i][j] = 0
                return
    print(np.matrix(sudoku))

print(automate())