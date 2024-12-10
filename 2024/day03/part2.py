import re

total = 0
active = True

with open('./input.txt') as file:
    line = file.readline().strip()

    while line:
        matches = re.findall(r'do\(\)|don\'t\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)', line)

        for match in matches:
            if match == "do()":
                active = True
            elif match == "don't()":
                active = False
            elif active:
                groups = re.search(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', match)
                total += int(groups.group(1)) * int(groups.group(2))

        line = file.readline().strip()

print("Result:", total)