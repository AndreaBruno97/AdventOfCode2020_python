''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

curr_x = 0
curr_y = 0
'''
    Current direction expressed as index in a circular array of directions:
    going right is +1 mod 4
    going left is -1 mod 4
    going forward is the same direction
'''
direction_array = ["E", "S", "W", "N"]
curr_direction = 0

for line_dirty in content:
    line = line_dirty.replace("\n", "")
    instruction = line[0]
    instruction_value = int(line[1:])


    # Change current direction before executing the movement
    if instruction == "L":
        degrees = int(instruction_value/90)
        curr_direction = (curr_direction - degrees) % 4
        continue
    elif instruction == "R":
        degrees = int(instruction_value/90)
        curr_direction = (curr_direction + degrees) % 4
        continue
    elif instruction == "F":
        instruction = direction_array[curr_direction]

    if instruction == "N":
        curr_y += instruction_value
    elif instruction == "S":
        curr_y -= instruction_value
    elif instruction == "E":
        curr_x += instruction_value
    elif instruction == "W":
        curr_x -= instruction_value


manhattan_distance = abs(curr_x) + abs(curr_y)
print("The Manhattan distance from the start is " + str(manhattan_distance))