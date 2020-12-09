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
for index in range(len(list) - preamble):

    previous = list[index:index+preamble]
    current = list[index+preamble]

    if not isValid(previous, current):
        ''' current is the first number that violates the rule '''
        first_violation = current
        break

if first_violation == 0:
    print("There's no number that violates the rule")
else:
    print("The first number that violates the rule is " + str(first_violation))