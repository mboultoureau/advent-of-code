safe_count = 0

def validate(levels):
    is_increasing = levels[1] > levels[0]

    for i in range(1, len(levels)):
        diff = abs(levels[i] - levels[i - 1])
        if (
            (diff < 1 or diff > 3) or
            (is_increasing and levels[i] < levels[i - 1]) or
            (not is_increasing and levels[i] > levels[i - 1])
        ):
            return (False, i)
    
    return (True, 0)

with open('./input.txt') as file:
    line = file.readline()
    while line:
        levels = [int(item) for item in line.strip().split(' ')]
        result, pos1 = validate(levels)
    
        if result:
            safe_count += 1
            line = file.readline()
            continue

        # Try removing the value
        val1 = levels[pos1]
        levels.pop(pos1)
        result, _ = validate(levels)

        if result:
            safe_count += 1
            line = file.readline()
            continue

        # Try removing the value before
        levels.insert(pos1, val1)
        levels.pop(pos1 - 1)
        result, _ = validate(levels)

        if result:
            safe_count += 1
            line = file.readline()
            continue
        
        line = file.readline()

print('Safe count:', safe_count)