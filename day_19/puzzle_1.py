
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
            if(len(curr_rule) == 1):
                rules[curr_key]["set"].add(str1)
            else:
                for str2 in rules[curr_rule[1]]["set"]:
                    rules[curr_key]["set"].add(str1+str2)

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

total = 0
for input in input_string.split("\n"):
    if input in rules["0"]["set"]:
        total +=1

print("The number of strings that respect the rules is " + str(total))
