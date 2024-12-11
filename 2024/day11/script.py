import os
from collections import Counter, defaultdict, deque

def read_file(filename):

    directory_path = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(directory_path, filename)

    with open(input_path) as file:
        return [int(stone) for stone in file.readline().strip().split(' ')]
    
def blink(stones):
    i = 0
    while i < len(stones):
        if stones[i] == 0:
            stones[i] = 1
        elif len(str(stones[i])) % 2 == 0:
            stone = str(stones[i])
            stones[i] = int(stone[:len(stone) // 2])
            stones.insert(i + 1, int(stone[len(stone) // 2:]))
            i += 1
        else:
            stones[i] *= 2024

        i += 1

    return stones

def smart_blink(stones):
    queue = deque(stones.items())
    stones = defaultdict(int)

    while len(queue) > 0:
        value, count = queue.pop()
        if value == 0:
            stones[1] += count
        elif len(str(value)) % 2 == 0:
            stone = str(value)
            stones[int(stone[:len(stone) // 2])] += count
            stones[int(stone[len(stone) // 2:])] += count
        else:
            stones[value * 2024] += count

    return stones



if __name__ == "__main__":
    # Part 1
    stones = read_file('input.txt')
    BLINK_COUNT = 25

    for _ in range(BLINK_COUNT):
        stones = blink(stones)

    print("[PART1] Number of stones:", len(stones))


    # Part 2
    stones = read_file('input.txt')
    stones = Counter(stones)
    BLINK_COUNT = 75

    for _ in range(BLINK_COUNT):
        stones = smart_blink(stones)

    total = 0
    for value, count in stones.items():
        total += count 

    print("[PART2] Number of stones:", total)