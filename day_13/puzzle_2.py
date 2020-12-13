''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

bus_list_dirty = content[1].replace("\n", "").split(",")

bus_list = []
for bus_index, bus_dirty in enumerate(bus_list_dirty):
    if bus_dirty == "x":
        continue
    bus_list.append({"id": int(bus_dirty), "offset": bus_index})

'''
Solution from lizthegrey ( https://www.twitch.tv/lizthegrey ):
https://www.twitch.tv/videos/835702252?t=00h24m11s

Each bus must satisfy the rule:
    timestamp + offset % id == 0
    
So, once we find the timestamp that satisfies the first equation,
we can arbitrairly add to it the value of id, without changing its vaule mod id.

Given that, we can increment the timestamp each time by a multiple of the id found, 
until we find a timestamp that satisfies also the second equation.
Like the first time, if we sum n times the second id to this timestamp, the second equation
remains satisfied, and if we continue adding (first_id * second_id) to the timestamp,
we continue to keep both equation satisfied. 

During the n-th iteration, if we increment the current timestamp with the product of all the previous ids,
we preserve the correctness of the previous n-1 equations, while continuing to search for the right timestamp
for equation n.

At the end of all ids, we have the timestamp that satisfies all the equations.
'''
product_of_previous_ids = 1
timestamp = 0
for bus in bus_list:
    while not (timestamp + bus["offset"]) % bus["id"] == 0:
        timestamp += product_of_previous_ids
    product_of_previous_ids *= bus["id"]

print("The correct timestamp is "+ str(timestamp))