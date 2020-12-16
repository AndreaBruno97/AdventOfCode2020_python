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
    rules[name] = {"min1": min1, "min2": min2, "max1": max1, "max2": max2}

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

Auxiliary structure: array of flags to check if a number is valid for any rule
'''

error_rate = 0
for cur_ticket in tickets:
    for field_str in cur_ticket:
        field =int(field_str)
        if field > len(enforce_any_rule) or enforce_any_rule[field] == 0:
            error_rate += field

print("The total ticket scanning error rate is " + str(error_rate))