from collections import defaultdict

numbers_before = defaultdict(set)
result = 0

def is_update_valid(pages):
    for i in range(len(pages)):
        rules = numbers_before[pages[i]]
        for j in range(i + 1, len(pages)):
            if pages[j] in rules:
                return False
            
    return True


with open('./input.txt') as file:
    line = file.readline().strip()
    # First part
    while line != "":
        before, page = line.split('|')
        numbers_before[page].add(before)
        line = file.readline().strip()

    line = file.readline().strip()

    # Second part
    while line:
        pages = line.split(',')
        if is_update_valid(pages):
            result += int(pages[len(pages) // 2])

        line = file.readline().strip()

print("Sum of middle pages:", result)