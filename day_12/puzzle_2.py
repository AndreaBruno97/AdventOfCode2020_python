''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

curr_x = 0
curr_y = 0
curr_waypoint_x = 10
curr_waypoint_y = 1

for line_dirty in content:
    line = line_dirty.replace("\n", "")
    instruction = line[0]
    instruction_value = int(line[1:])

    if instruction == "L":
        '''
        Anticlockwise rotation swaps the x and y directions and changes the sign of the new X value
        So, an even number of rotations leaves the x and y unswapped
        and, depending on the number of turns, the sign of the coordinates changes:
        0 ->  +1 +1 (nothing to change)
        1 ->  -1 +1
        2 ->  -1 -1
        3 ->  +1 -1
        '''
        degrees = int(instruction_value/90) % 4
        if not degrees % 2 == 0:
            tmp = curr_waypoint_x
            curr_waypoint_x = curr_waypoint_y
            curr_waypoint_y = tmp

        if degrees == 1:
            curr_waypoint_x *= -1
        elif degrees == 2:
            curr_waypoint_x *= -1
            curr_waypoint_y *= -1
        elif degrees == 3:
            curr_waypoint_y *= -1

    elif instruction == "R":
        '''
        Clockwise rotation swaps the x and y directions and changes the sign of the new Y value
        So, an even number of rotations leaves the x and y unswapped
        and, depending on the number of turns, the sign of the coordinates changes:
        0 ->  +1 +1 (nothing to change)
        1 ->  +1 -1
        2 ->  -1 -1
        3 ->  -1 +1
        '''
        degrees = int(instruction_value/90) % 4
        if not degrees % 2 == 0:
            tmp = curr_waypoint_x
            curr_waypoint_x = curr_waypoint_y
            curr_waypoint_y = tmp

        if degrees == 1:
            curr_waypoint_y *= -1
        elif degrees == 2:
            curr_waypoint_x *= -1
            curr_waypoint_y *= -1
        elif degrees == 3:
            curr_waypoint_x *= -1

    elif instruction == "F":
        curr_x += curr_waypoint_x * instruction_value
        curr_y += curr_waypoint_y * instruction_value

    elif instruction == "N":
        curr_waypoint_y += instruction_value
    elif instruction == "S":
        curr_waypoint_y -= instruction_value
    elif instruction == "E":
        curr_waypoint_x += instruction_value
    elif instruction == "W":
        curr_waypoint_x -= instruction_value

manhattan_distance = abs(curr_x) + abs(curr_y)
print("The Manhattan distance from the start is " + str(manhattan_distance))