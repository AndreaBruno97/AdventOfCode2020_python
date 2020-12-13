import sys
import math

''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

start_depart_time = int(content[0].replace("\n", ""))
bus_list = content[1].replace("\n", "").split(",")

earliest_bus_id = 0
min_waiting_time = sys.maxsize

for bus in bus_list:
    if bus == "x":
        continue

    curr_bus_id = int(bus)
    # This is the time from the last bus to the start departure time given by the input
    curr_time_from_start = start_depart_time % curr_bus_id
    curr_waiting_time = (curr_bus_id - curr_time_from_start) % curr_bus_id

    if curr_waiting_time < min_waiting_time:
        earliest_bus_id = curr_bus_id
        min_waiting_time = curr_waiting_time

result = earliest_bus_id * min_waiting_time
print("The bus ID multiplied by the minutes of waiting is " + str(result))