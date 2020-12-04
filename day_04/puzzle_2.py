''' Module for regular expressions '''
import re

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

    ''' dictionary of fields: key is field name, value is the value '''
    fields_and_values = line.split(" ")
    fields = {}
    for e in fields_and_values:
        fields[e.split(":")[0]] = e.split(":")[1]

    ''' check if the list of fields has all the correct elements
     with or without cid, regardless of the order
     if not, pass over it'''
    if(set(fields) != set(list_with_cid)) and (set(fields) != set(list_without_cid)):
        continue

    ''' Checks on the required fields '''
    pattern_byr = re.compile("^19[2-9][0-9]|200[0-2]$")
    if not pattern_byr.search(fields["byr"]):
        continue

    pattern_iyr = re.compile("^201[0-9]|2020$")
    if not pattern_iyr.search(fields["iyr"]):
        continue

    pattern_eyr = re.compile("^202[0-9]|2030$")
    if not pattern_eyr.search(fields["eyr"]):
        continue

    pattern_hgt = re.compile("^(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in$")
    if not pattern_hgt.search(fields["hgt"]):
        continue

    pattern_hcl = re.compile("^#[0-9a-f]{6}$")
    if not pattern_hcl.search(fields["hcl"]):
        continue

    pattern_ecl = re.compile("^amb|blu|brn|gry|grn|hzl|oth$")
    if not pattern_ecl.search(fields["ecl"]):
        continue

    pattern_pid = re.compile("^[0-9]{9}$")
    if not pattern_pid.search(fields["pid"]):
        continue

    correct_passports += 1

print("There are " + str(correct_passports) + " correct passports")