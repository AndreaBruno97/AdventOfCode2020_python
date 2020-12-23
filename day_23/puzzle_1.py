''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

cups = [int(x) for x in list(content)]
rounds = 100

cur_index = 0
cur_val = 0
size = len(cups)
for i in range(rounds):
    print("-- move {} --".format(i+1))
    cur_val = cups[cur_index]
    cups_print = cups.copy()
    cups_print[cur_index] = "(" + str(cur_val) + ")"
    print("cups: " + " ".join([str(x) for x in cups_print]))
    c1 = cups.pop((min(cur_index, size-1) + 1) % (size) )
    c2 = cups.pop((min(cur_index, size-2) + 1) % (size - 1) )
    c3 = cups.pop((min(cur_index, size-3) + 1) % (size - 2) )
    print("pick up: {}, {}, {}".format(c1, c2, c3))

    min_val = min(cups)
    max_val = max(cups)

    dest_val = cur_val
    for delta in range(3):
        dest_val -=1
        if dest_val<min_val:
            dest_val = max_val

        if not (dest_val == c1 or dest_val == c2 or dest_val == c3) :
            break



    print("Destination {}".format(dest_val))
    print()

    dest_index = cups.index(dest_val)
    cups.insert(dest_index + 1, c1)
    cups.insert(dest_index + 2, c2)
    cups.insert(dest_index + 3, c3)

    cur_index = ( cups.index(cur_val) + 1) % size

print("-- final --")
cur_val = cups[cur_index]
cups_print = cups.copy()
cups_print[cur_index] = "(" + str(cur_val) + ")"
print("cups: " + " ".join([str(x) for x in cups_print]))
print()

output = ""
start_index = cups.index(1)
cur_output_index = ( start_index + 1 ) % size
while not start_index == cur_output_index:
    output += str(cups[cur_output_index])
    cur_output_index = ( cur_output_index + 1) % size

print("The labels after 1 are " + output)