''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

adapters = []
for line_dirty in content:
    line = line_dirty.replace("\n", "")
    adapters.append(int(line))

adapters.sort()
# The outlet is first and has 0 jolts
adapters.insert(0, 0)

'''
The counter array contains the number of ways that each adapter can be reached
and it's updated by each adapter that adds their counter to each one that they reach
'''
counter = [0] * len(adapters)
counter[0] = 1


for current_index, current_adapter in enumerate(adapters):
    index  = current_index + 1
    if index >= len(adapters):
        continue

    while adapters[index] - current_adapter <= 3:
        counter[index] += counter[current_index]
        index += 1
        if index >= len(adapters):
            break

total_counter = counter[len(adapters)-1]
print("There are {} total combinations".format(total_counter))