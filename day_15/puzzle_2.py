''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

last_turn = 30000000
start_list = content.replace("\n", "").split(",")

'''
last_spoken is a dictionary that keeps track 
of the last turn a number was spoken in. 
'''
last_spoken = {}
last_num = ""
curr_num = ""
for turn in range (1, last_turn + 1):

    if turn <= len(start_list):
        curr_num = str(start_list[turn - 1])
    elif last_num in last_spoken.keys():
        curr_num = str( (turn - 1) - int(last_spoken[last_num]) )
    else:
        curr_num = "0"

    last_spoken[last_num] = str(turn-1)
    last_num = curr_num

print("The 30000000 number spoken is " + str(curr_num))