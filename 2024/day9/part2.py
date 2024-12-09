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
            disk_map.append({'id': '.', 'count': int(d)})
        else:
            disk_map.append({'id': str(id), 'count': int(d)})
            id += 1

        is_free_space = not is_free_space

    return disk_map

def smart_defragment(disk_map):
    for i in range(len(disk_map) - 1, -1, -1):
        if disk_map[i]['id'] == '.':
            continue

        for j in range(0, i):
            if disk_map[j]['id'] == '.' and disk_map[j]['count'] >= disk_map[i]['count']:
                remaining = disk_map[j]['count'] - disk_map[i]['count']
                disk_map[j]['id'] = disk_map[i]['id']
                disk_map[j]['count'] = disk_map[i]['count']
                disk_map[i]['id'] = '.'
                
                if remaining > 0:
                    disk_map.insert(j + 1, {'id': '.', 'count': remaining})

                break

    return disk_map

def display_disk_map(disk_map):
    line = ''
    for d in disk_map:
        line += d['id'] * d['count']
    print(line)

def calculate_checksum(defragmented_disk_map):
    checksum = 0
    j = 0
    for i in range(len(defragmented_disk_map)):
        if defragmented_disk_map[i]['id'] == '.':
            j += defragmented_disk_map[i]['count']
            continue
        
        for _ in range(defragmented_disk_map[i]['count']):
            checksum += int(defragmented_disk_map[i]['id']) * j
            j += 1

    return checksum


if __name__ == "__main__":
    line = read_file('input.txt')
    disk_map = expand_disk_map(line)
    defragmented_disk_map = smart_defragment(disk_map)
    checksum = calculate_checksum(defragmented_disk_map)

    print('Checksum:', checksum)