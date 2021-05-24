import numpy as np


class Tile:
    def __init__(self, id, matrix):
        self.id = id
        self.count = 0
        self.matrix = matrix

        self.spins = 0
        self.is_h_flipped = False
        self.is_v_flipped = False
        self.final_row = 0
        self.final_col = 0

    def sides(self):
        return [self.matrix[0],
                self.matrix[:, -1],
                self.matrix[-1][::-1],
                self.matrix[::-1, 0]]

    def flipped_sides(self):
        return [self.matrix[0][::-1],
                self.matrix[::-1, -1],
                self.matrix[-1],
                self.matrix[:, 0]]

    def current_sides(self):
        cur_matrix = np.rot90(self.matrix, self.spins, (1, 0))
        if self.is_h_flipped: cur_matrix = np.fliplr(cur_matrix)
        if self.is_v_flipped: cur_matrix = np.flipud(cur_matrix)
        return [cur_matrix[0],
                cur_matrix[:, -1],
                cur_matrix[-1][::-1],
                cur_matrix[:, 0]]

    def inside_matrix(self):
        cur_matrix = np.rot90(self.matrix, self.spins, (1, 0))
        if self.is_h_flipped: cur_matrix = np.fliplr(cur_matrix)
        if self.is_v_flipped: cur_matrix = np.flipud(cur_matrix)
        cur_matrix = np.delete(cur_matrix, [0, -1], 0)
        cur_matrix = np.delete(cur_matrix, [0, -1], 1)

        return cur_matrix

    # def current_matrix(self):
    #     cur_matrix = np.rot90(self.matrix, self.spins, (1, 0))
    #     if self.is_h_flipped: cur_matrix = np.fliplr(cur_matrix)
    #     if self.is_v_flipped: cur_matrix = np.flipud(cur_matrix)
    #
    #     return cur_matrix


class Match:
    def __init__(self, id_1, id_2, dir_1, dir_2, is_flipped):
        self.id_1 = id_1
        self.id_2 = id_2
        self.dir_1 = dir_1
        self.dir_2 = dir_2
        self.is_flipped = is_flipped
        # id_1 must spin (dir_2 - dir_1 + 2) times
        self.spin_num_1 = (dir_2 - dir_1 + 2) % 4
        # id_2 must spin (dir_1 - dir_2 + 2) times
        self.spin_num_2 = (dir_1 - dir_2 + 2) % 4


''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

tiles = []
rows = -1
matches = []
for tile_dirty in content.split("\n\n"):
    [title, matrix_str] = tile_dirty.split(":\n")
    id = title.replace("Tile ", "")

    rows = matrix_str.count("\n") + 1
    matrix = np.array(list([[int(x == "#")] for x in matrix_str.replace("\n", "")])).reshape(rows, rows)
    # matrix = np.array(list([x for x in matrix_str.replace("\n", "")])).reshape(rows, rows)
    tiles.append(Tile(id, matrix))

for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        side_num_i = 0
        for side_i in np.concatenate([tiles[i].sides(), tiles[i].flipped_sides()]):
            side_num_j = 0
            for side_j in tiles[j].sides():
                if np.array_equal(side_i, side_j):
                    #                    first id    second id    first side    second side      is_flipped
                    matches.append(
                        Match(tiles[i].id, tiles[j].id, side_num_i % 4, side_num_j % 4, 1 - int(side_num_i / 4)))
                    tiles[i].count += 1
                    tiles[j].count += 1
                side_num_j += 1

            side_num_i += 1

'''
The first tile is positioned in the middle, without spinning or flipping.
Each new tile is chosen from the list of tiles connected to the ones already placed
Its number of spins is the sum of the ones indicated in the Match object 
    and the ones the tile it's connected to already did
Its vertical or horizontal spin (depending on its final direction) is the sum of 
    the isFlipped flag in the match and the flip flag in the tile it's connected to
'''
pending_tiles = [{"id": x.id, "value": x} for x in tiles]
positioned_tiles = [pending_tiles.pop(0)]

while len(pending_tiles) > 0:
    # pending_indexes = [x["id"] for x in pending_tiles]
    # positioned_indexes = [x["id"] for x in positioned_tiles]
    border_tiles = set(
        [x.id_1 for x in matches if x.id_2 in [x["id"] for x in positioned_tiles]] + [x.id_2 for x in matches if
                                                                                      x.id_1 in [x["id"] for x in
                                                                                                 positioned_tiles]])

    cur_tile = [x for x in pending_tiles if x["id"] in border_tiles][0]

    cur_match_list = [m for m in matches if m.id_1 == cur_tile["id"] and m.id_2 in [x["id"] for x in positioned_tiles]]

    if len(cur_match_list) == 0:
        # match in which cur_tile is in position 2
        cur_match_list = [m for m in matches if
                          m.id_2 == cur_tile["id"] and m.id_1 in [x["id"] for x in positioned_tiles]]
        cur_match = cur_match_list[0]
        cur_positioned = [p for p in positioned_tiles if p["id"] == cur_match.id_1][0]
        dir_tile = cur_match.dir_2
        dir_positioned = cur_match.dir_1 + cur_positioned["value"].spins
        is_flipped = cur_match.is_flipped
        spin = cur_match.spin_num_2
    else:
        # match in which cur_tile is in position 1
        cur_match = cur_match_list[0]
        cur_positioned = [p for p in positioned_tiles if p["id"] == cur_match.id_2][0]
        dir_tile = cur_match.dir_1
        dir_positioned = cur_match.dir_2 + cur_positioned["value"].spins
        is_flipped = cur_match.is_flipped
        spin = cur_match.spin_num_1

    if dir_positioned == 0:
        # new tile up
        cur_tile["value"].final_col = cur_positioned["value"].final_col
        cur_tile["value"].final_row = cur_positioned["value"].final_row - (
            1 if not cur_positioned["value"].is_v_flipped else -1)
    elif dir_positioned == 1:
        # new tile right
        cur_tile["value"].final_col = cur_positioned["value"].final_col + (
            1 if not cur_positioned["value"].is_h_flipped else -1)
        cur_tile["value"].final_row = cur_positioned["value"].final_row
    elif dir_positioned == 2:
        # new tile down
        cur_tile["value"].final_col = cur_positioned["value"].final_col
        cur_tile["value"].final_row = cur_positioned["value"].final_row + (
            1 if not cur_positioned["value"].is_v_flipped else -1)
    else:
        # new tile left
        cur_tile["value"].final_col = cur_positioned["value"].final_col - (
            1 if not cur_positioned["value"].is_h_flipped else -1)
        cur_tile["value"].final_row = cur_positioned["value"].final_row

    cur_tile["value"].spins = (cur_positioned["value"].spins + spin) % 4

    if dir_positioned == 1 or dir_positioned == 3:
        # to the left or to the right, flip is vertical
        cur_tile["value"].is_h_flipped = cur_positioned["value"].is_h_flipped
        cur_tile["value"].is_v_flipped = bool((cur_positioned["value"].is_v_flipped + is_flipped) % 2)
    else:
        # up or down, flip is horizontal
        cur_tile["value"].is_h_flipped = bool((cur_positioned["value"].is_h_flipped + is_flipped) % 2)
        cur_tile["value"].is_v_flipped = cur_positioned["value"].is_v_flipped

    positioned_tiles.append(cur_tile)
    pending_tiles = [x for x in pending_tiles if not x["id"] == cur_tile["id"]]

positioned_tiles = [x["value"] for x in positioned_tiles]

ext_len = int(np.sqrt(len(positioned_tiles)))
int_len = len(positioned_tiles[0].inside_matrix()[0])
tot_len = ext_len * int_len
positioned_tiles = sorted(positioned_tiles, key=lambda x: (x.final_row, x.final_col))

completed_matrix = np.array([])

for ext_row in range(ext_len):
    for int_row in range(int_len):
        for col in range(ext_len):
            cur_tile = (ext_row * ext_len) + col
            completed_matrix = np.append(completed_matrix, positioned_tiles[cur_tile].inside_matrix()[int_row])

completed_matrix = completed_matrix.reshape(tot_len, tot_len)

base_monster = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
]
num_monster_elems = np.sum(base_monster)

monster_list = [
    base_monster,
    np.rot90(base_monster, 1),
    np.rot90(base_monster, 2),
    np.rot90(base_monster, 3),
    np.flipud(base_monster),
    np.rot90(np.flipud(base_monster), 1),
    np.rot90(np.flipud(base_monster), 2),
    np.rot90(np.flipud(base_monster), 3)
]

total_monsters = 0
for monster in monster_list:
    monster_rows = len(monster)
    monster_cols = len(monster[0])
    total_monsters = 0

    for row in range(tot_len - monster_rows):
        for col in range(tot_len - monster_cols):
            sub_matrix = completed_matrix[np.ix_(range(row, row + monster_rows), range(col, col + monster_cols))]

            curr_count = np.sum(np.multiply(monster, sub_matrix))
            total_monsters += (curr_count == num_monster_elems)

    if total_monsters > 0:
        break

print("The total number of # without monsters is " + str(int(np.sum(completed_matrix) - (total_monsters * num_monster_elems))))
