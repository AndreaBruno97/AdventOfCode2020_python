''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

valid_counter = 0

for line in content:
    [min_max, target_char_dirty, password] = line.split(" ")
    min_num = int(min_max.split("-")[0])
    max_num = int(min_max.split("-")[1])
    target_char = target_char_dirty[:-1]

    '''
    min_num, max_num
        minimum and maximum number of occurrences of target char
    target_char
        character to be counted in the password
    password
        password in which target characters are searched
    '''

    total_occurrences = 0
    ''' Count occurrences of target_char'''
    for char in password:
        total_occurrences += (char == target_char)

    if (total_occurrences >= min_num) and (total_occurrences <= max_num):
        valid_counter += 1

print("Total correct passwords: " + str(valid_counter))