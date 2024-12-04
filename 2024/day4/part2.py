import re
from collections import defaultdict

count = 0
lines = []

with open('./input.txt') as file:
    for line in file.readlines():
        lines.append(list(line.strip()))


for row in range(len(lines) - 2):
    for col in range(len(lines[0]) - 2):
        if (
            ((lines[row][col] == "M" and lines[row + 2][col + 2] == "S") or (lines[row][col] == "S" and lines[row + 2][col + 2] == "M")) and
            lines[row + 1][col + 1] == "A" and
            ((lines[row + 2][col] == "M" and lines[row][col + 2] == "S") or (lines[row + 2][col] == "S" and lines[row][col + 2] == "M"))
        ):
            count += 1

print('Count:', count)