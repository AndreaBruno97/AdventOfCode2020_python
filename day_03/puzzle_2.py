''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

module = len(content[0][:-1])
total_product = 1

for slope_x, slope_y in zip([1, 3, 5, 7, 1], [1, 1, 1, 1, 2]):
    trees = 0
    current_x = 0

    for index, line_dirty in enumerate(content):
        ''' check if the line has to be skipped, given the current slope_y'''
        if index % slope_y != 0:
            continue

        ''' The last character is \n, so it must be removed '''
        line = line_dirty[:-1]
        trees += (line[current_x] == "#")

        ''' 
        The next point in the next line is given by (old + 3) mod N, 
        where N is the length of each line
        '''
        current_x = (current_x + slope_x) % module

    total_product *= trees

print("The product of the trees of each slope is " + str(total_product))