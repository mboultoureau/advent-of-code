import re
from collections import defaultdict

count = 0
lines = []

with open('./input.txt') as file:
    for line in file.readlines():
        lines.append(list(line.strip()))


def number_of_occurences(line):
    string = ''.join(line)
    reversed_string = ''.join(reversed(line))
    occurences = len(re.findall(r'XMAS', string)) + len(re.findall(r'XMAS', reversed_string))
    return occurences

# Count horizontally
for line in lines:
    count += number_of_occurences(line)

# Count vertically
for col in range(len(lines[0])):
    line = []
    for row in range(len(lines)):
        line.append(lines[row][col])

    count += number_of_occurences(line)

# Count diagonally
def traverse_diagonally(start_row, start_col, row_increment, col_increment):
    line = []
    row, col = start_row, start_col
    while 0 <= row < len(lines) and 0 <= col < len(lines[0]):
        line.append(lines[row][col])
        row += row_increment
        col += col_increment
    return line


# Count diagonally (top-left to bottom-right)
for row in range(len(lines)):
    count += number_of_occurences(traverse_diagonally(row, 0, 1, 1))
for col in range(1, len(lines[0])):
    count += number_of_occurences(traverse_diagonally(0, col, 1, 1))

# Count diagonally (bottom-right to top-left)
for row in range(len(lines)):
    count += number_of_occurences(traverse_diagonally(row, 0, -1, 1))
for col in range(1, len(lines[0])):
    count += number_of_occurences(traverse_diagonally(len(lines) - 1, col, -1, 1))

print("Count:", count)