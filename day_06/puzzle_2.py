''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

''' Split the input into groups, since each one is divided by two newlines '''
groups_list = content.split("\n\n")

total = 0

for group_dirty in groups_list:
    ''' I create a list of answers of each person in the group '''
    group = group_dirty.split("\n")

    group_set = set(group[0])
    for answer in group:
        answer_set = set(answer)
        ''' In group_set remain only the answers that are common to both sets '''
        group_set.intersection_update(answer_set)

    total += len(group_set)

print("The total count is " + str(total))