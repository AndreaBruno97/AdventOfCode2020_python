def isValid(previous, current):
    '''
    In the sorted list, we can interrupt the inner iteration
    when the sum is higher than the current value
    '''

    previous.sort()

    for index_first in range(len(previous)):
        index_second = index_first + 1
        while index_second < len(previous):
            first = previous[index_first]
            second = previous[index_second]
            total = first + second

            if total < current:
                index_second += 1
                continue
            elif total > current:
                break

            return True

    return False


''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

preamble = 25
list = []
for item_dirty in content:
    item = item_dirty.replace("\n", "")

    list.append(int(item))

first_violation = -1
first_violation_index = -1
for index in range(len(list) - preamble):

    previous = list[index:index+preamble]
    current = list[index+preamble]

    if not isValid(previous, current):
        ''' current is the first number that violates the rule '''
        first_violation = current
        first_violation_index = index + preamble
        break

right_index_start = -1
right_index_end = -1

for index_start in range(len(list) - 1):
    index_end = index_start + 1
    total = list[index_start]
    while index_end < len(list):
        total += list[index_end]

        if total == first_violation:
            right_index_start = index_start
            right_index_end = index_end
            break
        elif total > first_violation:
            break

        index_end += 1

    if not right_index_start == -1:
        break

max_number = max(list[right_index_start:right_index_end+1])
min_number = min(list[right_index_start:right_index_end+1])
encryption_weakness = max_number + min_number

print("The encryption weakness is: " + str(encryption_weakness))