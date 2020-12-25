''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

subject_num = 7
pub_key_card, pub_key_door = [int(x) for x in content.split("\n")]

loop_size_card = 0
cur_pub_key_card = 1
while True:
    loop_size_card += 1
    cur_pub_key_card = (cur_pub_key_card * subject_num) % 20201227
    if cur_pub_key_card == pub_key_card:
        break

encryption_key = 1
for i in range(loop_size_card):
    encryption_key = (encryption_key * pub_key_door) % 20201227

print("The encryption key is {}".format(encryption_key))