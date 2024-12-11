f = open("input2.txt", "r")
lines = f.readlines()
size = len(lines[0].strip())

print(f"Size: {size} x {size}")

max_score = 0

for y in range(1, size - 1):
    for x in range(1, size - 1):
        # Tree to check
        tree = int(lines[y][x])

        # Check if visible
        left = list(map(int, lines[y][0:x]))
        left_score = 0
        for c in reversed(left):
            left_score += 1
            if c >= tree:
                break

        right = list(map(int, lines[y][x + 1:size]))
        right_score = 0
        for c in right:
            right_score += 1
            if c >= tree:
                break

        top_score = 0
        for c in reversed(lines[0:y]):
            top_score += 1
            if int(c[x]) >= tree:
                break

        bottom_score = 0
        for c in lines[y + 1:size]:
            bottom_score += 1
            if int(c[x]) >= tree:
                break

        score = left_score * right_score * top_score * bottom_score
        if score > max_score:
            max_score = score

print(f"Max score: {max_score}")
