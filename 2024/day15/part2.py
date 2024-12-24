import os
from collections import deque

def readfile(filename):
    directory_path = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(directory_path, filename)

    warehouse = []
    movements = []
    position = (0, 0)

    r, c = 0, 0

    with open(input_path) as file:
        line = file.readline()
        while line.strip() != '':
            row = []
            for char in line.strip():
                if char == '#':
                    row.extend(['#', '#'])
                elif char == 'O':
                    row.extend(['[', ']'])
                elif char == '.':
                    row.extend(['.', '.'])
                else:
                    row.extend(['.', '.'])
                    position = (r, c)
                
                c += 2

            r += 1
            c = 0
            warehouse.append(row)
            line = file.readline()

        while line:
            movements.extend(list(line.strip()))
            line = file.readline()



    return warehouse, movements, position

def move(warehouse, source, vector):
    r, c = (source[0] + vector[0], source[1] + vector[1])
    displacements = set()
    queue = deque([(r, c)])
    visited = set()

    # Check if it can move
    while queue:
        r, c = queue.pop()

        if (r, c) in visited:
            continue

        visited.add((r, c))

        if warehouse[r][c] == '#':
            return False
        elif warehouse[r][c] == '.':
            continue
        
        displacements.add((r + vector[0], c + vector[1], r, c))
        queue.append((r + vector[0], c + vector[1]))

        if warehouse[r][c] == '[':
            displacements.add((r + vector[0], c + vector[1] + 1, r, c + 1))
            queue.append((r + vector[0], c + vector[1] + 1))
            visited.add((r, c + 1))
        elif warehouse[r][c] == ']':
            displacements.add((r + vector[0], c + vector[1] - 1, r, c - 1))
            queue.append((r + vector[0], c + vector[1] - 1))
            visited.add((r, c - 1))



    # Move
    displacements = sorted(displacements)
    if vector[0] == 1 or vector[1] == 1:
        displacements = reversed(displacements)

    for nr, nc, r, c in displacements:
        print(nr, nc, r, c)
        warehouse[nr][nc] = warehouse[r][c]
        warehouse[r][c] = '.'

    return True
    
def move_robot(warehouse, position, movement):
    if movement == '^':
        vector = (-1, 0)
    elif movement == '>':
        vector = (0, 1)
    elif movement == '<':
        vector = (0, -1)
    else:
        vector = (1, 0)

    if move(warehouse, position, vector):
        position = (position[0] + vector[0], position[1] + vector[1])

    warehouse[position[0]][position[1]] = '.'

    return warehouse, position

def print_warehouse(warehouse, position):
    HEIGHT = len(warehouse)
    WIDTH = len(warehouse[0])

    for r in range(HEIGHT):
        row = ''
        for c in range(WIDTH):
            if (r, c) == position:
                row += '@'
            else:
                row += warehouse[r][c]
        print(row)

    print('\n\n')

def calculate_sum(warehouse):
    HEIGHT = len(warehouse)
    WIDTH = len(warehouse[0])

    result = 0
    for r in range(HEIGHT):
        for c in range(WIDTH):
            if warehouse[r][c] == '[':
                result += r * 100 + c

    return result

def main():
    warehouse, movements, position = readfile('input.txt')
    
    print('Initial state')
    print_warehouse(warehouse, position)

    for movement in movements:
        # print('Movement:', movement)
        warehouse, position = move_robot(warehouse, position, movement)
        # print_warehouse(warehouse, position)

    print_warehouse(warehouse, position)

    result = calculate_sum(warehouse)
    print('Result:', result)

if __name__ == "__main__":
    main()