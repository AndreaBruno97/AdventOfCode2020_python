''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

valid_counter = 0

for line in content:
    [indexes, target_char_dirty, password] = line.split(" ")
    first_index = int(indexes.split("-")[0])
    second_index = int(indexes.split("-")[1])
    target_char = target_char_dirty[:-1]

    '''
    first_index, second_index
        first and second index for  occurrences of target char
    target_char
        character to be compared in the password
    password
        password in which target characters are compared
    '''

    ''' Check if the password doesn't contain the selected indexes'''
    if len(password) < max(first_index,second_index):
        break

    first_matches = target_char == password[first_index - 1]
    second_matches = target_char == password[second_index - 1]

    if first_matches != second_matches:
        valid_counter += 1

print("Total correct passwords: " + str(valid_counter))