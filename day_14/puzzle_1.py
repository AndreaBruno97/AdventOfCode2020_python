''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

'''
In order to set al bits of the mask at 1 and 0, 
two masks can be used, 
    - one that has the 1s of the original masks (replace Xs with 0s) and sets the 1s of the value with an OR
    - one that has the 0s of the original masks (replace Xs with 1s) and sets the 0s of the value with an AND
'''

memory = {}
or_mask = 0
and_mask = 0
for instruction_dirty in content:
    instruction = instruction_dirty.replace("\n", "")

    if "mask" in instruction:
        # Mask update instruction
        mask = instruction.replace("mask = ", "")
        or_mask_string = mask.replace("X", "0")
        and_mask_string = mask.replace("X", "1")

        or_mask = int(or_mask_string, 2)
        and_mask = int(and_mask_string, 2)

    else:
        # Memory write instruction
        [address, value] = instruction.replace("mem[", "").split("] = ")
        value = int(value) | or_mask
        value = value & and_mask
        memory[address] = value

sum = 0
for value in memory.values():
    sum += int(value)

print("The sum of all values in memory is " + str(sum))