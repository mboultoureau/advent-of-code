f = open("input2.txt", "r")
lines = f.readlines()
total_score = 0

for line in lines:
    opponent = line.strip().split(" ")[0]
    choice = line.strip().split(" ")[1]

    score = 0

    # Score for the shape selected
    if choice == 'X':
        score += 1
    elif choice == 'Y':
        score += 2
    else:
        score += 3

    # Score for the outcome of the round
    if (
        (opponent == 'A' and choice == 'X') or
        (opponent == 'B' and choice == 'Y') or
        (opponent == 'C' and choice == 'Z')
    ):
        score += 3
    elif (
        (opponent == 'A' and choice == 'Y') or
        (opponent == 'B' and choice == 'Z') or
        (opponent == 'C' and choice == 'X')
    ):
        score += 6

    total_score += score


print("Total score:", total_score)