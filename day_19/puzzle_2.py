
def generateSet(rules, curr_key, max_size):
    if rules[curr_key]["value1"][0] == "a" or rules[curr_key]["value1"][0] == "b":
        rules[curr_key]["set"].add(rules[curr_key]["value1"][0])
        return rules

    for curr_rule in [rules[curr_key]["value1"], rules[curr_key]["value2"]]:
        if curr_rule is None:
            continue

        for curr_val in curr_rule:
            rules = generateSet(rules, curr_val, max_size)

        for str1 in rules[curr_rule[0]]["set"]:
            if len(curr_rule) == 1:
                rules[curr_key]["set"].add(str1)
                if curr_key == "8":
                    for i in range(int(max_size/len(str1))+1):
                        rules[curr_key]["set"].add(str1 * (i+1))

            else:
                for str2 in rules[curr_rule[1]]["set"]:
                    rules[curr_key]["set"].add(str1+str2)
                    if curr_key == "11":
                        for i in range(int(max_size/len(str1))+1):
                            rules[curr_key]["set"].add((str1 * (i+1)) + (str2 * (i+1)))

    return rules


''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

[rules_string, input_string] = content.split("\n\n")

input = rules_string.split("\n")
max_size = -1
for inp in input:
    if len(inp) > max_size:
        max_size = len(inp)

rules = {}
for rule_dirty in input:
    [key, values] = rule_dirty.replace("\"", "").split(": ")
    if "|" in values:
        [value_1, value_2] = values.split(" | ")
        value_1 = value_1.split(" ")
        value_2 = value_2.split(" ")
    else:
        value_1 = values.split(" ")
        value_2 = None

    rules[key] = {"value1": value_1, "value2": value_2, "set": set()}

rules = generateSet(rules, "0", max_size)

total = 0
for input in input_string.split("\n"):
    if input in rules["0"]["set"]:
        total +=1

print("The number of strings that respect the rules is " + str(total))
