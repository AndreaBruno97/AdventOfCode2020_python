def recursiveCombat(deck_1, deck_2):
    previous_decks_1 = []
    previous_decks_2 = []

    while len(deck_1) and len(deck_2):
        val_1 = deck_1.pop(0)
        val_2 = deck_2.pop(0)

        if deck_1 in previous_decks_1 and deck_2 in previous_decks_2:
            return 1, deck_1

        previous_decks_1.append(deck_1.copy())
        previous_decks_2.append(deck_2.copy())

        if val_1 > val_2:
            round_winner = 1
        else:
            round_winner = 2

        if val_1 <= len(deck_1) and val_2 <= len(deck_2):
            round_winner, winner_deck_tmp = recursiveCombat(deck_1[:val_1].copy(), deck_2[:val_2].copy())

        if round_winner == 1:
            deck_1.append(val_1)
            deck_1.append(val_2)
        else:
            deck_2.append(val_2)
            deck_2.append(val_1)

    if len(deck_1):
        return 1, deck_1
    else:
        return 2, deck_2

''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

deck_1_str, deck_2_str = content.replace("Player 1:\n", "").replace("Player 2:\n", "").split("\n\n")
deck_1 = [int(x) for x in deck_1_str.split("\n")]
deck_2 = [int(x) for x in deck_2_str.split("\n")]

winner_flag, winner = recursiveCombat(deck_1, deck_2)

final_score = 0
for i in range(len(winner)):
    final_score += winner[i] * (len(winner) - i)

print("The final score is: " + str(final_score))