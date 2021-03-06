import re

def enforceRules(rules, colors, current, counter):

    if current not in rules.keys():
        ''' This bag can't be contained by any other bag '''
        return colors, counter

    for next in rules[current]:
        ''' Search for all the bags that can contain the current one '''
        if colors[next] == 1:
            ''' This bag was already marked '''
            continue

        colors[next] = 1
        counter +=1
        colors, counter = enforceRules(rules, colors, next, counter)

    return colors, counter

''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

''' 
Initialization of the dictionaries: 
rules
        key is the inner bag 
        value is the set of bags that can contain it
colors
        key is the color
        value is 0 (later set to 1 if it can contain the target)
'''
rules = {}
colors = {}
for line in content:
    line = line.replace(".\n", "")
    [outer, inner_dirty] = line.split(" bags contain")

    colors[outer] = 0

    if inner_dirty == " no other bags":
        continue

    inner_dirty = re.sub(r" [0-9]+ ", "", inner_dirty)
    inner_dirty = re.sub(r" bag(s)?", "", inner_dirty)
    inner_list = inner_dirty.split(",")

    for inner in inner_list:
        if inner not in rules.keys():
            rules[inner] = set()

        rules[inner].add(outer)

target = "shiny gold"

counter = 0
result_colors, counter = enforceRules(rules, colors, target, counter)

''' Beware, the current solution is off by 1 for the given input '''
print("There are " + str(counter + 1) + " possible colors")
