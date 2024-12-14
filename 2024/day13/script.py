import os
import re

def read_file(filename):
    directory_path = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(directory_path, filename)

    machines = []

    with open(input_path) as file:
        machine = {
            'buttonA': [0, 0],
            'buttonB': [0, 0],
            'prize': [0, 0]
        }

        button_a_re = re.compile(r'Button A: X\+([0-9]+), Y\+([0-9]+)')
        button_b_re = re.compile(r'Button B: X\+([0-9]+), Y\+([0-9]+)')
        prize_re = re.compile(r'Prize: X=([0-9]+), Y=([0-9]+)')

        line = file.readline()
        while line:
            x, y = button_a_re.search(line).groups()
            machine['buttonA'] = [int(x), int(y)]

            line = file.readline()
            x, y = button_b_re.search(line).groups()
            machine['buttonB'] = [int(x), int(y)]

            line = file.readline()
            x, y = prize_re.search(line).groups()
            machine['prize'] = [int(x), int(y)]

            machines.append(machine.copy())

            line = file.readline()
            if line:
                line = file.readline()

    return machines

def solve(machines):
    PRICE_A = 3
    PRICE_B = 1
    result = 0

    for machine in machines:
        x1, y1 = machine['buttonA']
        x2, y2 = machine['buttonB']
        px, py = machine['prize']

        det = x1 * y2 - x2 * y1
        if det == 0:
            continue

        dx = px * y2 - py * x2
        dy = py * x1 - px * y1

        if dx % det != 0 or dy % det != 0:
            continue

        a = dx // det
        b = dy // det

        if a < 0 or b < 0:
            continue

        result += PRICE_A * a + PRICE_B * b

    return result

if __name__ == "__main__":
    machines = read_file('input.txt')
    result = solve(machines)
    print("[PART1] Result:", result)

    for i in range(len(machines)):
        machines[i]['prize'] = [machines[i]['prize'][0] + 10000000000000, machines[i]['prize'][1] + 10000000000000]
    
    result = solve(machines)
    print("[PART2] Result:", result)