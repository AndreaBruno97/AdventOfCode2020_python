''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

cups = [int(x) for x in list(content)]
max_num_cups = 1000000
for i in range(len(cups), max_num_cups + 1):
    cups.append(i)

rounds = 10000000

cur_index = 0
cur_val = 0
size = len(cups)
for i in range(rounds):
    not i%100 and print(str(i))
    cur_val = cups[cur_index]
    c1 = cups.pop((min(cur_index, size-1) + 1) % (size) )
    c2 = cups.pop((min(cur_index, size-2) + 1) % (size - 1) )
    c3 = cups.pop((min(cur_index, size-3) + 1) % (size - 2) )

    min_val = min(cups)
    max_val = max(cups)

    dest_val = cur_val
    for delta in range(3):
        dest_val -=1
        if dest_val<min_val:
            dest_val = max_val

        if not (dest_val == c1 or dest_val == c2 or dest_val == c3) :
            break


    dest_index = cups.index(dest_val)
    cups.insert(dest_index + 1, c1)
    cups.insert(dest_index + 2, c2)
    cups.insert(dest_index + 3, c3)

    cur_index = ( cups.index(cur_val) + 1) % size

start_index = cups.index(1)
first_val = ( start_index + 1 ) % size
second_val = ( start_index + 2 ) % size
output = first_val * second_val

print("The result is " + str(output))