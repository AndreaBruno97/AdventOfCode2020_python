''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

adapters = []
for line_dirty in content:
    line = line_dirty.replace("\n", "")
    adapters.append(int(line))

adapters.sort()

# The outlet has 0 jolts
previous = 0

'''
The array contains the counters for the number of differences, sorted.
Each slot counts the difference of n-1:
    counter_differences[0] -> 1-jolt difference
    counter_differences[1] -> 2-jolts difference
    counter_differences[2] -> 3-jolts difference
3-jolts difference starts at 1, since the last adapter is always 3 jolts higher than the highest in the list
'''
counter_differences = [0, 0, 1]

for current_adapter in adapters:
    difference = current_adapter - previous
    counter_differences[difference - 1] += 1
    previous = current_adapter

diff_1 = counter_differences[0]
diff_3 = counter_differences[2]
product = diff_1 * diff_3
print("There are {} differences of 1 and {} differences of 3\n{} * {} = {}".format(diff_1, diff_3, diff_1, diff_3, product))