import re


class Color:
    def __init__(self, name, num):
        self.name = name
        self.num = num


def enforceRules(rules, colors, current, counter):
    inner_counter = 0

    if current not in rules.keys():
        ''' This bag can't contain any other bag '''
        return colors, counter, 0

    for next in rules[current]:
        ''' Search for all the bags that can be contained by the current one '''

        colors[next.name] = 1
        counter += 1
        colors, counter, tmp_counter = enforceRules(rules, colors, next.name, counter)
        inner_counter += (tmp_counter + 1) * next.num

    return colors, counter, inner_counter


''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

''' 
Initialization of the dictionaries: 
rules
        key is the outer bag 
        value is the set of inner bags and their number
colors
        key is the color
        value is 0 (later set to 1 if it can contain the target)
'''
rules = {}
colors = {}
for line in content:
    line = line.replace(".", "").replace("\n", "")
    [outer, inner_dirty] = line.split(" bags contain ")

    colors[outer] = 0

    if inner_dirty == "no other bags":
        continue
    inner_dirty = re.sub(r" bag(s)?", "", inner_dirty)

    inner_list = inner_dirty.split(", ")

    for inner in inner_list:
        [inner_num, inner_name] = inner.split(" ", 1)
        if outer not in rules.keys():
            rules[outer] = set()

        rules[outer].add(Color(inner_name, int(inner_num)))

target = "shiny gold"
counter = 0


result_colors, counter, cumulative_counter = enforceRules(rules, colors, target, counter)

print("There are " + str(cumulative_counter) + " possible colors")
