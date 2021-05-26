def neighbours(x, y):
    return [
        (x+1, y),
        (x, y+1),
        (x+1, y-1),
        (x-1, y),
        (x, y-1),
        (x-1, y+1),
    ]

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

# max_len = max([len(x) for x in directions])
# max_size = (2 * max_len) + (2 * rounds ) + 3
# matrix = np.zeros((max_size, max_size))
# Set of coordinates of black tiles
matrix = set()

for cur_dir in directions:
    cur_x = 0
    cur_y = 0

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

    # matrix[cur_x, cur_y] = 1 - matrix[cur_x, cur_y]
    position = (cur_x, cur_y)
    if position in matrix:
        # tile was black and now it's white
        matrix.remove(position)
    else:
        # tile was white and now it's black
        matrix.add(position)

for round in range(rounds):
    matr_tmp = matrix.copy()

    # for i in range(1,max_size-1):
    #     for j in range(1,max_size-1):
    #
    #         near_black_tiles = matrix[i+1, j] + matrix[i,j+1] +\
    #                            matrix[i-1,j+1] + matrix[i-1,j] +\
    #                             matrix[i,j-1] + matrix[i+1,j-1]
    #
    #         if matrix[i, j] == 1 and (near_black_tiles == 0 or near_black_tiles > 2):
    #             matr_tmp[i,j] = 0
    #         if matrix[i, j] == 0 and (near_black_tiles == 2):
    #             matr_tmp[i, j] = 1

    for (cur_x, cur_y) in matrix:
        cur_neighbours = neighbours(cur_x, cur_y)
        near_black_tiles = sum(int(x in matrix) for x in cur_neighbours)
        if(near_black_tiles == 0 or near_black_tiles > 2):
            matr_tmp.remove((cur_x,cur_y))

        for near_white in filter(lambda x: x not in matrix, cur_neighbours):
            near_black_tiles = sum([int(x in matrix) for x in neighbours(near_white[0], near_white[1])])
            if(near_black_tiles == 2):
                matr_tmp.add(near_white)

    matrix = matr_tmp.copy()

# output = int(np.sum(matrix))
output = len(matrix)
print("The total number of black tiles is " + str(output))
