f = open("input.txt", "r")
lines = f.readlines()

horizontal = 0
depth = 0

for line in lines:
    line = line.split()
    if line[0] == "forward":
        horizontal += int(line[1])
    elif line[0] == "down":
        depth += int(line[1])
    elif line[0] == "up":
        depth -= int(line[1])

print(horizontal, depth, horizontal * depth)