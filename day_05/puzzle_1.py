''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

max_row = -1
max_column = -1
max_id = -1

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

    ''' Convert the string (in binary) to the row's and column's numbers (in decimal) '''
    row = int(row_binary_string, 2)
    column = int(column_binary_string, 2)
    id = ( row * 8 ) + column

    if id > max_id:
        max_id = id
        max_row = row
        max_column = column

print("The highest seat ID is " + str(max_id) + " in row " + str(max_row) + " and column " + str(max_column))