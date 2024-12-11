f = open("input2.txt", "r")
lines = f.readlines()
size = len(lines[0].strip())

print(f"Size: {size} x {size}")

nb_visibles = 0

for y in range(1, size - 1):
    for x in range(1, size - 1):
        # Tree to check
        tree = int(lines[y][x])
        visible = False

        # Check if visible
        left = list(map(int, lines[y][0:x]))
        if all(x < tree for x in left):
            nb_visibles += 1
            continue

        right = list(map(int, lines[y][x + 1:size]))
        if all(x < tree for x in right):
            nb_visibles += 1
            continue

        top = []
        for c in lines[0:y]:
            top.append(int(c[x]))
        if all(x < tree for x in top):
            nb_visibles += 1
            continue

        bottom = []
        for c in lines[y + 1:size]:
            bottom.append(int(c[x]))
        if all(x < tree for x in bottom):
            nb_visibles += 1

print(f"{nb_visibles} visible trees in the interior")
print(f"{size * 4 - 4} visible trees on the edge")

# Count visibles in exterior
nb_visibles += size * 4 - 4

print(f"Visible trees: {nb_visibles}")