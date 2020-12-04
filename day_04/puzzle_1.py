''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()
content = content.split("\n\n")

list_with_cid = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
list_without_cid = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
correct_passports = 0

for line_dirty in content:
    ''' Modify input file in array of passports: each field is only separated by spaces '''
    line = line_dirty.replace("\n", " ")

    ''' array of fields without value '''
    fields_and_values = line.split(" ")
    fields = []
    for e in fields_and_values:
        fields.append(e.split(":")[0])

    ''' check if the list of fields has all the correct elements
     with or without cid, regardless of the order'''
    if(set(fields) == set(list_with_cid)) or (set(fields) == set(list_without_cid)):
        correct_passports += 1

print("There are " + str(correct_passports) + " correct passports")