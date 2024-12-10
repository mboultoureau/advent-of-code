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
        return set()
    
    if map[r][c] != current:
        return set()
    
    if current == 9:
        return {f"{r}.{c}"}

    trailheads = set()
    directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

    for d in directions:
        trailheads.update(count(d[0], d[1], current + 1, map))

    return trailheads

if __name__ == "__main__":
    sum = 0
    map = read_file('example.txt')

    NB_ROWS = len(map)
    NB_COLS = len(map[0])

    for r in range(NB_ROWS):
        for c in range(NB_COLS):
            trailheads = count(r, c, 0, map)
            sum += len(trailheads)

            # if len(trailheads) > 0:
            #     print(len(trailheads), end=" ")

    print("Sum:", sum)