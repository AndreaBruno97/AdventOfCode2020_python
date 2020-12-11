import numpy as np

def newRound(old_matrix, rows, cols):

    newMatrix = np.copy(old_matrix)
    for cur_row in range(rows):
        for cur_col in range(cols):

            '''
            Iteration for every point in the matrix,
            they're sourrounded by a submatrix of size 3x3:
                
                x-1,y-1     x-1,y   x-1,y+1 
                
                x,y-1       x,y     x,y+1
                
                x+1,y-1     x+1,y   x+1,y+1
                
            but not when x or y have values 0 or len-1
            In that case the submatrix is smaller
            '''
            row_min = max(0, cur_row-1)
            row_max = min(rows-1, cur_row+1)
            col_min = max(0, cur_col-1)
            col_max = min(cols-1, cur_col+1)

            submatrix = old_matrix[row_min:row_max+1, col_min:col_max+1]
            # Remember if the current seat is occupied, in that case it should be removed from the counter
            is_current_seat_occupied = 0
            if old_matrix[cur_row][cur_col] == "#":
                is_current_seat_occupied = 1

            # Compute the number of seats
            subarray = np.array(submatrix).reshape(-1)
            occupied_seats = np.shape(np.where(subarray == "#"))[1] - is_current_seat_occupied

            if old_matrix[cur_row][cur_col] == "L":
                if occupied_seats == 0:
                    newMatrix[cur_row][cur_col] = "#"
            elif old_matrix[cur_row][cur_col] == "#":
                if occupied_seats >= 4:
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
    newMatrix = newRound(matrix,rows,cols)
    if (newMatrix == matrix).all():
        # This round didn't change the matrix
        break
    matrix = newMatrix.copy()


matrix_into_array = np.array(matrix).reshape(-1)
occupied_seats = np.shape(np.where(matrix_into_array == "#"))[1]

print("There are " + str(occupied_seats) + " occupied seats")