import pprint

def generateSet(rules, curr_key):
    if rules[curr_key]["value1"][0] == "a" or rules[curr_key]["value1"][0] == "b":
        rules[curr_key]["set"].add(rules[curr_key]["value1"][0])
        return rules

    for curr_rule in [rules[curr_key]["value1"], rules[curr_key]["value2"]]:
        if curr_rule is None:
            continue

        for curr_val in curr_rule:
            rules = generateSet(rules, curr_val)

        for str1 in rules[curr_rule[0]]["set"]:
            if (len(curr_rule) == 1):
                rules[curr_key]["set"].add(str1)
            elif (len(curr_rule) == 2):
                for str2 in rules[curr_rule[1]]["set"]:
                    rules[curr_key]["set"].add(str1 + str2)
            elif (len(curr_rule) == 3):
                for str2 in rules[curr_rule[1]]["set"]:
                    for str3 in rules[curr_rule[2]]["set"]:
                        rules[curr_key]["set"].add(str1 + str2 + str3)

    return rules


''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

[rules_string, input_string] = content.split("\n\n")

rules = {}
for rule_dirty in rules_string.split("\n"):
    [key, values] = rule_dirty.replace("\"", "").split(": ")
    if "|" in values:
        [value_1, value_2] = values.split(" | ")
        value_1 = value_1.split(" ")
        value_2 = value_2.split(" ")
    else:
        value_1 = values.split(" ")
        value_2 = None

    rules[key] = {"value1": value_1, "value2": value_2, "set": set()}
rules = generateSet(rules, "0")
set_42 = rules["42"]["set"]
set_31 = rules["31"]["set"]
total = 0

# Each element in set_42 and set_31 has the same length
match_size = len(list(set_42)[0])

for input in input_string.split("\n"):
    input_set = [input[i:i+match_size] for i in range(0, len(input), match_size)]
    num_42 = 0
    num_31 = 0

    while len(input_set) > 0 and input_set[0] in set_42:
        input_set.pop(0)
        num_42 += 1

    while len(input_set) > 0 and input_set[-1] in set_31:
        input_set.pop(-1)
        num_31 += 1

    if len(input_set) == 0 and num_42 >= 2 and num_31 >= 1 and num_42 > num_31:
        total += 1

print("The number of strings that respect the rules is " + str(total))
