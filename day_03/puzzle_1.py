''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

trees = 0
current_x = 0
module = len(content[0][:-1])

slope = 3

for line_dirty in content:
    ''' The last character is \n, so it must be removed '''
    line = line_dirty[:-1]
    trees += (line[current_x] == "#")

    ''' 
    The next point in the next line is given by (old + 3) mod N, 
    where N is the length of each line
    '''
    current_x = (current_x + slope) % module

print("There are " + str(trees) + " trees in the path")