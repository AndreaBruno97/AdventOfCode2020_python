''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

max_num_cups = 1000000
rounds = 10000000

# list of cups
cups = [int(x) for x in list(content)]

for i in range(len(cups), max_num_cups):
    cups.append(i+1)

# next cup for each cup (cup -> next cup)
next_cup = dict(zip(cups, cups[1:] + [cups[0]]))

cur_val = cups[0]
size = max_num_cups
min_val = min(cups)
max_val = max(cups)

for i in range(rounds):
    c1 = next_cup[cur_val]
    c2 = next_cup[c1]
    c3 = next_cup[c2]

    dest_val = cur_val
    while True:
        dest_val -=1
        if dest_val<min_val:
            dest_val = max_val

        if not (dest_val == c1 or dest_val == c2 or dest_val == c3) :
            break

    # Update next_index
    next_cup[cur_val] = next_cup[c3]
    next_cup[c3] = next_cup[dest_val]
    next_cup[dest_val] = c1

    cur_val = next_cup[cur_val]

first = next_cup[1]
second = next_cup[first]
output = first * second

print("The result is " + str(output))