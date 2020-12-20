import numpy as np

class Tile:
    def __init__(self, id, sides):
        self.id = id
        self.sides = sides
        self.count = 0
        self.flipped_sides = []
        for arr in sides:
            self.flipped_sides.append(arr[::-1])

''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

tiles = []
rows = -1
for tile_dirty in content.split("\n\n"):
    [title, matrix_str] = tile_dirty.split(":\n")
    id = title.replace("Tile ", "")

    rows = matrix_str.count("\n") + 1
    matrix = np.array(list(matrix_str.replace("\n", ""))).reshape(rows, rows)
    tiles.append(Tile(id, [matrix[0], matrix[-1], matrix[:,0], matrix[:,-1]]))

for i in range(len(tiles)):
    for j in range(i+1, len(tiles)):
        for side_i in np.concatenate([tiles[i].sides, tiles[i].flipped_sides]):
            for side_j in tiles[j].sides:
                if np.array_equal(side_i, side_j):
                    tiles[i].count +=1
                    tiles[j].count +=1

total = 1
for tile in tiles:
    if tile.count == 2:
        total *= int(tile.id)

print("The product of the IDs of the corner tiles is " + str(total))