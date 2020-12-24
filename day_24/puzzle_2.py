import numpy as np

''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()
directions = []
for line_dirty in content:
    cur_input = list(line_dirty.replace("\n", ""))
    cur_directions = []
    while len(cur_input):
        tmp = []
        tmp.append(cur_input.pop(0))
        if tmp[0] == "s" or tmp[0] == "n":
            tmp.append(cur_input.pop(0))

        cur_directions.append("".join(tmp))

    directions.append(cur_directions)

rounds = 100

max_len = max([len(x) for x in directions])
max_size = (2 * max_len) + (2 * rounds ) + 3
matrix = np.zeros((max_size, max_size))

for cur_dir in directions:
    cur_x = max_len + 1
    cur_y = max_len + 1

    for dir in cur_dir:
        if dir == "e":
            cur_y += 1
            cur_x -= 1
        elif dir == "se":
            cur_x -= 1
        elif dir == "sw":
            cur_y -= 1
        elif dir == "w":
            cur_x += 1
            cur_y -= 1
        elif dir == "nw":
            cur_x += 1
        elif dir == "ne":
            cur_y += 1

    matrix[cur_x, cur_y] = 1 - matrix[cur_x, cur_y]

for round in range(rounds):
    matr_tmp = matrix.copy()

    for i in range(1,max_size-1):
        for j in range(1,max_size-1):

            near_black_tiles = matrix[i+1, j] + matrix[i,j+1] +\
                               matrix[i-1,j+1] + matrix[i-1,j] +\
                                matrix[i,j-1] + matrix[i+1,j-1]

            if matrix[i, j] > 0.9 and (near_black_tiles < 0.1 or near_black_tiles > 2.9):
                matr_tmp[i,j] = 0
            if matrix[i, j] < 0.1 and (near_black_tiles > 1.9 and near_black_tiles < 2.1):
                matr_tmp[i, j] = 1
    matrix = matr_tmp.copy()

output = int(np.sum(matrix))
print("The total number of black tiles is " + str(output))
