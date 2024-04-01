import time
import sudoku

grid = []

for i in range(9):
    row = list(input("Row: ")) # ['1'. '2', '3', ...]
    ints = []

    for n in row:
        ints.append(int(n)) # [1, 2, 3, 4, ...]
    grid.append(ints)
    print("Row " + str(i) + "completed!")

time.sleep(5)

def print(board):
    str_matrix = []

    for num in grid:
        str_matrix.append(str(num))
    return str_matrix

print(sudoku.solve(grid))
print(sudoku.print_board(grid))






#600000002
#709036000
#005480090
#830000007
#140065928
#950817630
#000670205
#500000460
#008004000