import numpy as np


def newRound(old_matrix, size_x, size_y, size_z, size_w):
    newMatrix = np.copy(old_matrix)
    for cur_w in range(size_w):
        for cur_z in range(size_z):
            for cur_y in range(size_y):
                for cur_x in range(size_x):

                    '''
                    Iteration for every point in the matrix,
                    they're sourrounded by a submatrix of size 3x3x3:
    
                        (same for [w-1,z-1], [w-1,z], [w,z-1])
    
                        w,z:    
                        x-1,y-1     x-1,y   x-1,y+1 
    
                        x,y-1       x,y     x,y+1
    
                        x+1,y-1     x+1,y   x+1,y+1
    
                        (same for [w+1,z+1], [w+1,z], [w,z+1])
    
                    but not when x, y, z or w have values 0 or len-1
                    In that case the submatrix is smaller
                    '''
                    x_min = max(0, cur_x - 1)
                    x_max = min(size_x - 1, cur_x + 1)
                    y_min = max(0, cur_y - 1)
                    y_max = min(size_y - 1, cur_y + 1)
                    z_min = max(0, cur_z - 1)
                    z_max = min(size_z - 1, cur_z + 1)
                    w_min = max(0, cur_w - 1)
                    w_max = min(size_w - 1, cur_w + 1)

                    submatrix = old_matrix[w_min:w_max + 1, z_min:z_max + 1, y_min:y_max + 1, x_min:x_max + 1]
                    # Remember if the current seat is occupied, in that case it should be removed from the counter
                    is_current_seat_occupied = old_matrix[cur_w][cur_z][cur_y][cur_x]
                    total_occupied = np.sum(submatrix) - is_current_seat_occupied

                    if is_current_seat_occupied:
                        if (not total_occupied == 2) and (not total_occupied == 3):
                            newMatrix[cur_w][cur_z][cur_y][cur_x] = 0
                    else:
                        if total_occupied == 3:
                            newMatrix[cur_w][cur_z][cur_y][cur_x] = 1

    return newMatrix


''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

rounds = 6
size = len(content)
# The final cube can expand outside the original cube by at most one space per round in each direction
max_size_x = size + (2 * rounds)
max_size_y = max_size_x
max_size_z = 1 + (2 * rounds)
max_size_w = max_size_z

matrix = np.array([])

# Elements below the original space
matrix = np.append(matrix, np.zeros((max_size_x * max_size_y * max_size_z * rounds), dtype=int))

# Elements below the original plane
matrix = np.append(matrix, np.zeros((max_size_x * max_size_y * rounds), dtype=int))

'''
Elements at z=0, but above the original square:
    ooooooo
    ooooooo
    ..xxx..
    ..xxx..
    ..xxx..
    .......
    .......
'''
matrix = np.append(matrix, np.zeros((max_size_y * rounds), dtype=int))

for line_dirty in content:
    '''
    Elements at z=0, but at the right and left of the original square:
        .......
        .......
        ooxxxoo
        ooxxxoo
        ooxxxoo
        .......
        .......
    '''
    matrix = np.append(matrix, np.zeros((rounds), dtype=int))
    line = line_dirty.replace("\n", "").replace(".", "0").replace("#", "1")
    matrix = np.append(matrix, [int(x) for x in list(line)])
    matrix = np.append(matrix, np.zeros((rounds), dtype=int))

'''
Elements at z=0, but above the original square:
    .......
    .......
    ..xxx..
    ..xxx..
    ..xxx..
    ooooooo
    ooooooo
'''
matrix = np.append(matrix, np.zeros((max_size_y * rounds), dtype=int))

# Elements above the original plane
matrix = np.append(matrix, np.zeros((max_size_x * max_size_y * rounds), dtype=int))

# Elements above the original space
matrix = np.append(matrix, np.zeros((max_size_x * max_size_y * max_size_z * rounds), dtype=int))

matrix = matrix.reshape(max_size_w, max_size_z, max_size_y, max_size_x)

newMatrix = np.array([])
for cur_round in range(rounds):
    newMatrix = newRound(matrix, max_size_x, max_size_y, max_size_z, max_size_w)
    matrix = newMatrix.copy()

active_cubes = int(np.sum(matrix))

print("There are " + str(active_cubes) + " active cubes")
