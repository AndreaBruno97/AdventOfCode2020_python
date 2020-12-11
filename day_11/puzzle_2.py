import numpy as np


def searchOccupied(matrix, rows, cols, curr_row, curr_col, delta_row, delta_col):
    '''
    This function moves in the matrix in the direction given by the deltas:

            -1,-1      -1,0     -1,+1

             0,-1       x       0,+1

            +1,-1      +1,0     +1,+1

    and returns 1 if the first seat it finds is a "#", otherwise 0

    '''
    search_row = curr_row + delta_row
    search_col = curr_col + delta_col

    while (search_row >= 0 and search_row < rows) and (search_col >= 0 and search_col < cols):
        if matrix[search_row][search_col] == "#":
            return 1
        elif matrix[search_row][search_col] == "L":
            return 0
        search_row += delta_row
        search_col += delta_col

    return 0


def newRound(old_matrix, rows, cols):
    newMatrix = np.copy(old_matrix)
    for cur_row in range(rows):
        for cur_col in range(cols):

            occupied_seats = 0
            for delta_row, delta_col in [[-1, -1], [-1, 0], [-1, +1], [0, -1], [0, +1], [+1, -1], [+1, 0], [+1, +1]]:
                occupied_seats += searchOccupied(matrix, rows, cols, cur_row, cur_col, delta_row, delta_col)

            if old_matrix[cur_row][cur_col] == "L":
                if occupied_seats == 0:
                    newMatrix[cur_row][cur_col] = "#"
            elif old_matrix[cur_row][cur_col] == "#":
                if occupied_seats >= 5:
                    newMatrix[cur_row][cur_col] = "L"

    return newMatrix


''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

rows = len(content)
# Not counting the \n
cols = len(content[0]) - 1

matrix = np.array([])
for line_dirty in content:
    line = line_dirty.replace("\n", "")
    matrix = np.append(matrix, list(line))
matrix = matrix.reshape(rows, cols)

newMatrix = np.array([])
while True:
    newMatrix = newRound(matrix, rows, cols)
    if (newMatrix == matrix).all():
        # This round didn't change the matrix
        break
    matrix = newMatrix.copy()

matrix_into_array = np.array(matrix).reshape(-1)
occupied_seats = np.shape(np.where(matrix_into_array == "#"))[1]

print("There are " + str(occupied_seats) + " occupied seats")