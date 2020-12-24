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

max_len = max([len(x) for x in directions])
max_size = (2 * max_len) + 1
matrix = np.zeros((max_size, max_size))

for cur_dir in directions:
    cur_x = max_len + 1
    cur_y = max_len + 1

    for dir in cur_dir:
        if dir == "e":
            cur_y += 1
            cur_x -=1
        elif dir == "se":
            cur_x -= 1
        elif dir == "sw":
            cur_y -= 1
        elif dir == "w":
            cur_x += 1
            cur_y -=1
        elif dir == "nw":
            cur_x += 1
        elif dir == "ne":
            cur_y += 1

    matrix[cur_x, cur_y] = 1 - matrix[cur_x, cur_y]

output  = int(np.sum(matrix))
print("The total number of black tiles is " + str(output))