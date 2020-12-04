TARGET_SUM = 2020

''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

''' Extract input in array '''
input_vet = []
for element in content:
    input_vet.append(int(element))
input_vet.sort()

''' 
Compute the sum:
Each number in the sorted list is summed to the ones after it.
When the sum is over the target, there's no need to try the other
elements in the inner loop
 '''
total = 0

for index_first, first in enumerate(input_vet):
    if index_first == len(input_vet) - 1:
        ''' The last element doesn't have any element after it to sum it to '''
        break

    index_second = index_first + 1
    total = 0

    while total <= TARGET_SUM:
        second = input_vet[index_second]
        total = first + second

        if total == TARGET_SUM:
            print("{} + {} = {}".format(first, second, total))
            print("Their product is " + str(first * second))
            break

        index_second += 1

    if total == TARGET_SUM:
        break

if total != TARGET_SUM:
    print("There's no couple of numbers that sum to " + str(TARGET_SUM))