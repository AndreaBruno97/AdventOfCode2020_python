''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

''' Split the input into groups, since each one is divided by two newlines '''
groups_list = content.split("\n\n")

total = 0

for group_dirty in groups_list:
    ''' I create a string of answers without spaces or newlines '''
    group = group_dirty.replace(" ", "").replace("\n", "")

    group_set = set(group)
    total += len(group_set)

print("The total count is " + str(total))