import os

directory_path = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(directory_path, "input.txt")

map = []
antinodes = []

with open(input_path) as file:
    line = file.readline().strip()
    while line:
        map.append(list(line))
        antinodes.append(list('.' * len(line)))
        line = file.readline().strip()

NB_ROWS = len(map)
NB_COLS = len(map[0])

for i1 in range(NB_ROWS * NB_COLS):
    r1 = i1 // NB_ROWS
    c1 = i1 % NB_COLS

    for i2 in range(i1 + 1, NB_ROWS * NB_COLS):
        r2 = i2 // NB_ROWS
        c2 = i2 % NB_COLS

        if map[r1][c1] == '.' or map[r1][c1] != map[r2][c2]:
            continue

        distance_r = r2 - r1
        distance_c = c2 - c1

        antinode1_r = r1 - distance_r
        antinode1_c = c1 - distance_c
        antinode2_r = r2 + distance_r
        antinode2_c = c2 + distance_c

        if antinode1_r >= 0 and antinode1_r < NB_ROWS and antinode1_c >= 0 and antinode1_c <= NB_COLS:
            antinodes[antinode1_r][antinode1_c] = '#'

        if antinode2_r >= 0 and antinode2_r < NB_ROWS and antinode2_c >= 0 and antinode2_c <= NB_COLS:
            antinodes[antinode2_r][antinode2_c] = '#'

def display_map(map, antinodes):
    for r in range(NB_ROWS):
        line = ''
        for c in range(NB_COLS):
            if map[r][c] != '.':
                line += map[r][c]
            elif antinodes[r][c] != '.':
                line += antinodes[r][c]
            else:
                line += '.'

        print(line)

display_map(map, antinodes)

locations = 0
for r in range(NB_ROWS):
    for c in range(NB_COLS):
        if antinodes[r][c] == '#':
            locations += 1

print('Unique locations:', locations)