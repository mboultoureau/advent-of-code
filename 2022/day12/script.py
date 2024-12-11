from collections import deque
import os

def read_file(filename):

    directory_path = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(directory_path, filename)

    with open(input_path) as file:
        heightmap = []
        source = (0, 0)
        destination = (0, 0)

        lines = file.readlines()

        for r in range(len(lines)):
            line = list(lines[r].strip())
            row = []
            for c in range(len(line)):
                if line[c] == 'S':
                    source = (r, c)
                    row.append(0)
                elif line[c] == 'E':
                    destination = (r, c)
                    row.append(25)
                else:
                    row.append(ord(line[c]) - ord('a'))

            heightmap.append(row)

    return heightmap, source, destination

def traverse(heightmap, source, destination):
    visited = set()
    queue = deque([(source[0], source[1], 0)])
    steps = 0

    NB_ROWS = len(heightmap)
    NB_COLS = len(heightmap[0])

    while queue:
        length = len(queue)
        for _ in range(length):
            row, col, steps = queue.popleft()
            if (row, col) == destination:
                return steps
            
            if (row, col) in visited:
                continue

            visited.add((row, col))

            movements = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for dr, dc in movements:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < NB_ROWS and 0 <= new_col < NB_COLS:
                    if heightmap[new_row][new_col] <= heightmap[row][col] + 1:
                        queue.append((new_row, new_col, steps + 1))
        steps += 1

    return -1


if __name__ == "__main__":
    # Part 1
    heightmap, source, destination = read_file('input.txt')
    steps = traverse(heightmap, source, destination)

    if steps == -1:
        print("[PART1] No path found")
    else:
        print("[PART1] Number of steps:", steps)

    # Part 2
    best_path = float("inf")
    for r in range(len(heightmap)):
        for c in range(len(heightmap[0])):
            if heightmap[r][c] == 0:
                steps = traverse(heightmap, (r, c), destination)
                if steps != -1:
                    best_path = min(steps, best_path)

    print("[PART2] Best steps", best_path)