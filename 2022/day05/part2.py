import re

f = open("input2.txt", "r")
lines = f.readlines()

nb_stacks = 0
stacks = []

# Get nb stacks
for line in lines:
    x = re.findall(r"([0-9]\s*)", line.strip())
    if len(x) > 0:
        nb_stacks = len(x)
        break

# Init stacks
for i in range(nb_stacks):
    stacks.append([])

# Parse each stack
for line in lines:
    # Check if is stack
    x = re.search(r"([0-9]\s*)", line.strip())
    if x != None:
        break

    # Parse stack
    for i in range(nb_stacks):
        letter = line[i * 4 + 1:(i + 1) * 4 - 2]
        if letter != ' ':
            stacks[i].append(letter)

# Movements
for line in lines:
    x = re.search(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)", line.strip())
    if x == None:
        continue

    nb_move = int(x.group(1))
    from_move = int(x.group(2))
    to_move = int(x.group(3))

    crates_to_move = []

    for i in range(nb_move):
        crate = stacks[from_move - 1].pop(0)
        crates_to_move.append(crate)

    stacks[to_move - 1] = crates_to_move + stacks[to_move - 1]

# Print result
result = ''
for i in range(nb_stacks):
    result += stacks[i][0]

print(result)