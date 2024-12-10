import time

def read_file(filename):
    lab_map = []
    guard_position = {
        "row": 0,
        "col": 0,
        "direction": "up"
    }

    row_idx = 0
    with open(filename) as file:
        line = file.readline().strip()

        while line:
            row = []
            for col_idx in range(len(line)):
                if line[col_idx] == '^':
                    guard_position = { 'row': row_idx, 'col': col_idx, 'direction': 'up' }
                    row.append('.')
                elif line[col_idx] == '>':
                    guard_position = { 'row': row_idx, 'col': col_idx, 'direction': 'right' }
                    row.append('.')
                elif line[col_idx] == 'v':
                    guard_position = { 'row': row_idx, 'col': col_idx, 'direction': 'down' }
                    row.append('.')
                elif line[col_idx] == '<':
                    guard_position = { 'row': row_idx, 'col': col_idx, 'direction': 'left' }
                    row.append('.')
                else:
                    row.append(line[col_idx])

            lab_map.append(row)

            row_idx += 1
            line = file.readline().strip()

    return lab_map, guard_position

def display_guard(direction):
    if direction == "up":
        return '^'
    elif direction == "right":
        return '>'
    elif direction == "down":
        return 'v'
    elif direction == 'left':
        return '<'

def display_map(lab_map, guard_position):
    nb_rows = len(lab_map)
    nb_cols = len(lab_map[0])

    colors = {
        "gray": "\033[90m",
        "red": "\033[31m",
        "yellow": "\033[33m",
        "reset": "\033[0m"
    }

    for row in range(nb_rows):
        line = ''
        for col in range(nb_cols):
            if guard_position["row"] == row and guard_position['col'] == col:
                line += display_guard(guard_position['direction'])
            elif lab_map[row][col] == '.':
                line += colors['gray'] + lab_map[row][col] + colors['reset']
            elif lab_map[row][col] == '|' or lab_map[row][col] == '-' or lab_map[row][col] == '+':
                line += colors['yellow'] + lab_map[row][col] + colors['reset']
            else:
                line += colors['red'] + lab_map[row][col] + colors['reset']

        print(line)

def clear_map(lab_map):
    line_up = '\033[1A'
    line_clear = '\x1b[2K'

    nb_rows = len(lab_map)
    for _ in range(nb_rows):
        print(line_up, end=line_clear)

def advance_player(lab_map, guard_position, distinct_positions):
    nb_rows, nb_cols = len(lab_map), len(lab_map[0])
    row = guard_position['row']
    col = guard_position['col']
    direction = guard_position['direction']

    if lab_map[row][col] != '|' and lab_map[row][col] != '-' and lab_map[row][col] != '+':
        distinct_positions += 1

    if lab_map[row][col] != '+':
        if direction == 'up' or direction == 'down':
            lab_map[row][col] = '|'
        else:
            lab_map[row][col] = '-'

    movements = {'up': [-1, 0], 'right': [0, 1], 'down': [1, 0], 'left': [0, -1]}
    movement = movements[direction]
    new_position = [row + movement[0], col + movement[1]]

    if new_position[0] < 0 or new_position[1] < 0 or new_position[0] >= nb_rows or new_position[1] >= nb_cols:
        return lab_map, guard_position, distinct_positions, True
    
    directions = ['up', 'right', 'down', 'left']
    if lab_map[new_position[0]][new_position[1]] == '#':
        lab_map[row][col] = '+'
        guard_position['direction'] = directions[(directions.index(direction) + 1) % 4]
    else:
        guard_position['row'] = new_position[0]
        guard_position['col'] = new_position[1]

    return lab_map, guard_position, distinct_positions, False

def place_obstacles(lab_map, guard_position):
    obstacles = []

    initial_map = [row.copy() for row in lab_map]
    initial_guard_position = guard_position.copy()

    nb_rows, nb_cols = len(lab_map), len(lab_map[0])
    for row in range(nb_rows):
        for col in range(nb_cols):
            if lab_map[row][col] == '#':
                continue

            lab_map = [row.copy() for row in initial_map]
            guard_position = initial_guard_position.copy()
            lab_map[row][col] = '#'

            # Check if the guard is looping
            previous_positions = set()
            is_looping = False
            finished = False

            while not finished:
                previous_positions.add((guard_position['row'], guard_position['col'], guard_position['direction']))
                lab_map, guard_position, _, finished = advance_player(lab_map, guard_position, 0)

                if finished:
                    break

                if (guard_position['row'], guard_position['col'], guard_position['direction']) in previous_positions:
                    is_looping = True
                    break

            if is_looping:
                obstacles.append((row, col))

    return obstacles

if __name__ == "__main__":
    lab_map, guard_position = read_file('./input.txt')
    distinct_positions = 0
    finished = False

    obstacles = place_obstacles(lab_map, guard_position)

    print(f"{len(obstacles)} are possibles.")