f = open("input2.txt", "r")
lines = f.readlines()
total_score = 0

for line in lines:
    opponent = line.strip().split(" ")[0]
    outcome = line.strip().split(" ")[1]
    choice = ''

    score = 0

    # Estimate outcome
    if outcome == 'X':
        if opponent == 'A':
            choice = 'C'
        elif opponent == 'B':
            choice = 'A'
        else:
            choice = 'B'
    elif outcome == 'Y':
        choice = opponent
    else:
        if opponent == 'A':
            choice = 'B'
        elif opponent == 'B':
            choice = 'C'
        else:
            choice = 'A'

    # Score for the shape selected
    if choice == 'A':
        score += 1
    elif choice == 'B':
        score += 2
    else:
        score += 3

    # Score for the outcome of the round
    if opponent == choice:
        score += 3
    elif (
        (opponent == 'A' and choice == 'B') or
        (opponent == 'B' and choice == 'C') or
        (opponent == 'C' and choice == 'A')
    ):
        score += 6

    total_score += score


print("Total score:", total_score)