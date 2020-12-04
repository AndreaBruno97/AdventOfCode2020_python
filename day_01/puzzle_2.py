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
    if index_first == len(input_vet) - 2:
        ''' The second-to-last element doesn't have any two elements after it to sum it to '''
        break

    index_second = index_first + 1

    while total <= TARGET_SUM:
        index_third = index_second + 1
        second = input_vet[index_second]

        while total <= TARGET_SUM:
            third = input_vet[index_third]
            total = first + second + third
            if total == TARGET_SUM:
                print("{} + {} + {} = {}".format(first, second, third, total))
                print("Their product is " + str(first * second * third))
                break

            index_third += 1

        index_second += 1
        if total == TARGET_SUM:
            break
        total = 0

    if total == TARGET_SUM:
        break
    total = 0

if total != TARGET_SUM:
    print("There're no three numbers that sum to " + str(TARGET_SUM))