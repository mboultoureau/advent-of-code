safe_count = 0

with open('./input.txt') as file:
    line = file.readline()
    while line:
        levels = [int(item) for item in line.strip().split(' ')]
        is_increasing = levels[1] > levels[0]
        valid = True

        for i in range(1, len(levels)):
            diff = abs(levels[i] - levels[i - 1])
            # print((diff < 1 or diff > 3))
            if (
                (diff < 1 or diff > 3) or
                (is_increasing and levels[i] < levels[i - 1]) or
                (not is_increasing and levels[i] > levels[i - 1])
            ):
                # print("Unsafe:", line)
                valid = False
                break
            

        if valid:
            # print("Safe:", line)
            safe_count += 1

        line = file.readline()

print('Safe count:', safe_count)