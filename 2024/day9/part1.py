import os

def read_file(filename):

    directory_path = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(directory_path, filename)

    with open(input_path) as file:
        return file.readline()

def expand_disk_map(line):
    disk_map = []
    id = 0
    is_free_space = False

    for d in line:
        if is_free_space:
            disk_map.extend(['.' for _ in range(int(d))])
        else:
            disk_map.extend([str(id) for _ in range(int(d))])
            id += 1

        is_free_space = not is_free_space

    return disk_map

def defragment(disk_map):
    i = 0
    j = len(disk_map) - 1

    while i < j:
        # Move i until free space
        if disk_map[i] != '.':
            i += 1
            continue

        # Move j until file
        if disk_map[j] == '.':
            j -= 1
            continue

        # Swap
        disk_map[i] = disk_map[j]
        disk_map[j] = '.'

    return disk_map

def calculate_checksum(defragmented_disk_map):
    checksum = 0
    for i in range(len(defragmented_disk_map)):
        if defragmented_disk_map[i] == '.':
            return checksum
        
        checksum += int(defragmented_disk_map[i]) * i

    return checksum


if __name__ == "__main__":
    line = read_file('input.txt')
    disk_map = expand_disk_map(line)
    defragmented_disk_map = defragment(disk_map)
    checksum = calculate_checksum(defragmented_disk_map)

    print('Checksum:', checksum)