import os

def read_file(filename):

    directory_path = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(directory_path, filename)

    with open(input_path) as file:
        return [[int(char) for char in line] for line in [line.strip() for line in file.readlines()]]
    
def count(r, c, current, map):
    NB_ROWS = len(map)
    NB_COLS = len(map[0])

    if r < 0 or r >= NB_ROWS or c < 0 or c >= NB_COLS:
        return 0
    
    if map[r][c] != current:
        return 0
    
    if current == 9:
        return 1

    trailheads = 0
    directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

    for d in directions:
        trailheads += count(d[0], d[1], current + 1, map)

    return trailheads

if __name__ == "__main__":
    sum = 0
    map = read_file('input.txt')

    NB_ROWS = len(map)
    NB_COLS = len(map[0])

    for r in range(NB_ROWS):
        for c in range(NB_COLS):
            trailheads = count(r, c, 0, map)
            sum += trailheads

            # if trailheads > 0:
            #     print(trailheads, end=" ")

    print("Sum:", sum)