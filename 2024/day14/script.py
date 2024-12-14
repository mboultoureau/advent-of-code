import os
import re
import time
from PIL import Image

def readfile(filename):
    directory_path = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(directory_path, filename)

    robots = []
    regex = r'p=(-?[0-9]+),(-?[0-9]+) v=(-?[0-9]+),(-?[0-9]+)'

    with open(input_path) as file:
        for line in file.readlines():
            x, y, vx, vy = re.search(regex, line).groups()
            robots.append([int(x), int(y), int(vx), int(vy)])

    return robots


def print_positions(robots, width, height):
    plan = [[0 for _ in range(width)] for _ in range(height)]
    for robot in robots:
        plan[robot[1]][robot[0]] += 1

    for r in range(height):
        line = ''
        for c in range(width):
            if plan[r][c] == 0:
                line += '.'
            else:
                line += str(plan[r][c])

        print(line)

def tick(robots, width, height):
    for i in range(len(robots)):
        x, y, vx, vy = robots[i]
        robots[i] = [
            (x + vx) % width,
            (y + vy) % height,
            vx,
            vy
        ]

    return robots

def calculate_safety(robots, width, height):
    q1, q2, q3, q4 = 0, 0, 0, 0
    for robot in robots:
        x, y, _, _ = robot
        if x < width // 2 and y < height // 2:
            q1 += 1
        elif x > width // 2 and y < height // 2:
            q2 += 1
        elif x < width // 2 and y > height // 2:
            q3 += 1
        elif x > width // 2 and y > height // 2:
            q4 += 1
    
    return q1 * q2 * q3 * q4

def clear_map(height):
    line_up = '\033[1A'
    line_clear = '\x1b[2K'

    for _ in range(height):
        print(line_up, end=line_clear)

def map_to_png(robots, width, height, filename):
    img = Image.new('RGB', (width, height), color = 'white')
    pixels = img.load()

    for robot in robots:
        x, y, _, _ = robot
        pixels[x, y] = (0, 0, 0)

    img.save(filename)

def is_probably_easter_eggs(robots, width, height):
    # Check if there is a 5x5 square with one robot minimum per cell
    plan = [[0 for _ in range(width)] for _ in range(height)]
    for robot in robots:
        plan[robot[1]][robot[0]] += 1

    for r in range(height - 4):
        for c in range(width - 4):
            count = 0
            for i in range(5):
                for j in range(5):
                    if plan[r + i][c + j] >= 1:
                        count += 1

            if count == 25:
                return True
            
    return False

def main():
    # Part 1
    WIDTH = 101 # Example: 11
    HEIGHT = 103 # Example: 7
    robots = readfile('input.txt')

    for s in range(100):
        robots = tick(robots, WIDTH, HEIGHT)

    print("[PART1]: Safety factor:", calculate_safety(robots, WIDTH, HEIGHT))


    # Part 2
    robots = readfile('input.txt')

    for s in range(10000):
        robots = tick(robots, WIDTH, HEIGHT)

        if is_probably_easter_eggs(robots, WIDTH, HEIGHT):
            print_positions(robots, WIDTH, HEIGHT)
            map_to_png(robots, WIDTH, HEIGHT, 'easter_eggs.png')
            print("[PART2]: Easter eggs found at second:", s + 1)
            break





if __name__ == "__main__":
    main()