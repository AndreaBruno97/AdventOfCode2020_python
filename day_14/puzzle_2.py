import re

'''
cur_pos = curr_mask.find("X")

    if cur_pos == -1:
        mask_list.append(int(curr_mask, 2))
        return mask_list

    new_mask_0 = list(curr_mask)
    new_mask_0[cur_pos] = "0"
    mask_list = generate_mask_list("".join(new_mask_0), mask_list)

    new_mask_1 = list(curr_mask)
    new_mask_1[cur_pos] = "1"
    mask_list = generate_mask_list("".join(new_mask_1), mask_list)

    return mask_list
    '''


def generate_address_list(address, address_list, x_positions, curr_pos):
    if curr_pos == len(x_positions):
        address_list.append(int(address, 2))
        return address_list

    new_addr_0 = list(address)
    new_addr_0[x_positions[curr_pos]] = "0"
    address_list = generate_address_list("".join(new_addr_0), address_list, x_positions, curr_pos+1)

    new_addr_1 = list(address)
    new_addr_1[x_positions[curr_pos]] = "1"
    address_list = generate_address_list("".join(new_addr_1), address_list, x_positions, curr_pos+1)

    return address_list

''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

'''
In order to set al bits of the mask at 1, only one mask is necessary:
    - one that has the 1s of the original masks (replace Xs with 0s) and sets the 1s of the address with an OR
    
To satisfy the constraint of the floating X, however, each input memory address must be updated with the n occurrences of Xs of the mask
and thus generating a list of 2^n addresses
'''

memory = {}
first_or_mask = 0
x_positions = []

for instruction_dirty in content:
    instruction = instruction_dirty.replace("\n", "")

    if "mask" in instruction:
        # Mask update instruction
        mask = instruction.replace("mask = ", "")
        first_or_mask_string = mask.replace("X", "0")
        first_or_mask = int(first_or_mask_string, 2)

        x_positions = []
        for x in re.finditer("X", mask):
            x_positions.append(x.start())


    else:
        # Memory write instruction
        [address, value] = instruction.replace("mem[", "").split("] = ")

        address_string = '{0:036b}'.format(int(address))
        address_list = generate_address_list(address_string, [], x_positions, 0)

        for new_address in address_list:
            new_address = new_address | first_or_mask
            memory[new_address] = int(value)


sum = 0
for value in memory.values():
    sum += int(value)

print("The sum of all values in memory is " + str(sum))