''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

[rules_dirty, all_tickets_dirty] = content.split("\n\nyour ticket:\n")
[my_ticket_dirty, tickets_dirty] = all_tickets_dirty.split("\n\nnearby tickets:\n")

rules_str = rules_dirty.split("\n")
tickets_str = tickets_dirty.split("\n")

rules = {}
absolute_max = -1
for rule in rules_str:
    [name, values] = rule.split(": ")
    [val1, val2] = values.split(" or ")
    [min1, max1] = val1.split("-")
    [min2, max2] = val2.split("-")

    min1 =int(min1)
    min2 =int(min2)
    max1 =int(max1)
    max2 =int(max2)
    rules[name] = {"min1": min1, "min2": min2, "max1": max1, "max2": max2, "tmp_positions": set(range(0, len(rules_str)))}

    if absolute_max < max2:
        absolute_max = max2

enforce_any_rule = [0] * (absolute_max + 1)
for cur_rule in rules.values():
    for i in range(cur_rule["min1"], cur_rule["max1"] + 1):
        enforce_any_rule[i] = 1
    for i in range(cur_rule["min2"], cur_rule["max2"] + 1):
        enforce_any_rule[i] = 1


my_ticket = my_ticket_dirty.split(",")
tickets = []
for ticket in tickets_str:
    fields = ticket.split(",")
    tickets.append(fields)

'''
rules is a dictionary of rules, the key is the name, the value is an object with the four extreme values for the two ranges

tickets is an array , in which each value is an array of fields of the same ticket

Auxiliary structures: 
    array of flags to check if a number is valid for any rule
    set in the rule, starts with all the possible position values, each one is deleted if there's a value that diproves that possibility
'''

for cur_index in reversed(range(0, len(tickets))):
    cur_ticket = tickets[cur_index]
    for field_str in cur_ticket:
        field =int(field_str)
        if field > len(enforce_any_rule) or enforce_any_rule[field] == 0:
            tickets.pop(cur_index)
            continue

# Now the tickets are filtered
for cur_ticket in tickets:
    for cur_index, cur_value_str in enumerate(cur_ticket):
        for cur_rule in rules.values():
            cur_value = int(cur_value_str)
            if ( len(cur_rule["tmp_positions"]) == 1 ) or ( not cur_index in cur_rule["tmp_positions"] ):
                continue

            if ( cur_value < cur_rule["min1"] or cur_value < cur_rule["min2"] ) and ( cur_value > cur_rule["max1"] or cur_value > cur_rule["max2"] ):
                # The value in that position can't be in that rule
                cur_rule["tmp_positions"].remove(cur_index)


'''
After the first filtering, there are some rules that only have one possible spot, and thus are already identified.
That spot, since it's already taken, must be deleted from the other rules, potentially creating other one-spot rules, and continuing the cycle until all the rule have only one spot.

For example, having these rules:
1) {1, 2}
2) {0, 1, 2}
3) {2}

Rule 3 is surely in position 2, so we can delete position 2 from the possible positions of the other rules:
[3] -> 2
1) {1}
2) {0, 1}

Now rule 1 can only be in position 1:
[3] -> 2
[1] -> 1
2) {0}

And thus rule 2 can only be in position 0:
[3] -> 2
[1] -> 1
[2] -> 0

'''

rules_found = {}

while len(rules) > 0:
    new_rule_name = [x for x in rules if len(rules[x]["tmp_positions"]) == 1][0]
    found_value = min(rules[new_rule_name]["tmp_positions"])
    rules_found[new_rule_name] = rules[new_rule_name]
    rules.pop(new_rule_name)
    for cur_rule in rules.values():
        if found_value in cur_rule["tmp_positions"]:
            cur_rule["tmp_positions"].remove(found_value)

product = 1
for field in rules_found:
    if not "departure" in field:
        continue

    index = int(min(rules_found[field]["tmp_positions"]))
    new_value = int(my_ticket[index])
    product *= new_value

print('The product of all fields containing "departure" is ' + str(product))