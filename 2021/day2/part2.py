f = open("input.txt", "r")
lines = f.readlines()

horizontal = 0
depth = 0
aim = 0

for line in lines:
    line = line.split()
    if line[0] == "forward":
        horizontal += int(line[1])
        depth += aim * int(line[1])
    elif line[0] == "down":
        aim += int(line[1])
    elif line[0] == "up":
        aim -= int(line[1])

print(horizontal, depth, horizontal * depth)