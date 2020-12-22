''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

deck_1_str, deck_2_str = content.replace("Player 1:\n", "").replace("Player 2:\n", "").split("\n\n")
deck_1 = [int(x) for x in deck_1_str.split("\n")]
deck_2 = [int(x) for x in deck_2_str.split("\n")]

while len(deck_1) and len(deck_2):
    val_1 = deck_1.pop(0)
    val_2 = deck_2.pop(0)

    if val_1 > val_2:
        deck_1.append(val_1)
        deck_1.append(val_2)
    else:
        deck_2.append(val_2)
        deck_2.append(val_1)

winner = []
if len(deck_1):
    winner = deck_1
else:
    winner = deck_2

final_score = 0
for i in range(len(winner)):
    final_score += winner[i] * (len(winner) - i)

print("The final score is: " + str(final_score))