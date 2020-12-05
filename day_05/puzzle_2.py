''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

id_list = []

for line in content:
    ''' Delete final space '''
    line = line.replace("\n", "")
    ''' Row is composed by the first 7 characters, Column is the lst three '''
    row_string = line[:7]
    column_string = line[-3:]

    '''
    Binary search strings correspond to the binary representation
    of row and column position, with 
        F->0, B->1 for row,
        L->0, R->1 for column            
    '''
    row_binary_string = row_string.replace("F", "0").replace("B", "1")
    column_binary_string = column_string.replace("L", "0").replace("R", "1")

    ''' Convert the string (in binary) to the row's and coumn's numbers (in decimal) '''
    row = int(row_binary_string, 2)
    column = int(column_binary_string, 2)
    id = ( row * 8 ) + column

    id_list.append(id)

my_row = -1
my_column = -1
my_id = -1

'''
id_list, when sorted, contains all the IDs from a to b, except the target ID x:
a, a+1, a+2, [...], x-2, x-1, (Here there's no x) x+1, x+2, [...], b-2, b-1, b 
'''
id_list.sort()
for index, current_id in enumerate(id_list):
    if index == 0:
        continue

    if current_id - id_list[index-1] != 1:
        ''' 
        Found the gap:
            current_id is x+1, the next ID
            id_list[index-1] is x-1, the previous ID
        '''
        my_id = current_id - 1
        my_column = my_id % 8
        my_row = int((my_id - my_column) / 8)
        break

print("My seat ID is " + str(my_id) + " in row " + str(my_row) + " and column " + str(my_column))