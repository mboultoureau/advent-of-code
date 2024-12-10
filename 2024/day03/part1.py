import re

total = 0

with open('./input.txt') as file:
    line = file.readline().strip()

    while line:
        matches = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', line)
        for match in matches:
            groups = re.search(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', match)
            total += int(groups.group(1)) * int(groups.group(2))

        line = file.readline().strip()

print("Result:", total)