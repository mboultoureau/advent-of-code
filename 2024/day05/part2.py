from collections import defaultdict

numbers_before = defaultdict(set)
result = 0

def is_update_valid(pages):
    for i in range(len(pages)):
        rules = numbers_before[pages[i]]
        for j in range(i + 1, len(pages)):
            if pages[j] in rules:
                return i
            
    return -1

def fix_update(pages, invalid_index):
    is_valid = False
    invalid_page = pages[invalid_index]
    rules = numbers_before[invalid_page]

    while not is_valid:
        is_valid = True

        # Move the invalid index to right
        pages.pop(invalid_index)
        invalid_index += 1
        pages.insert(invalid_index, invalid_page)

        # Check invalid index is now at the right place
        for i in range(invalid_index + 1, len(pages)):
            if pages[i] in rules:
                is_valid = False

    return pages

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
        invalid_index = is_update_valid(pages)
        if invalid_index == -1:
            line = file.readline().strip()
            continue

        fixed_pages = []
        while invalid_index != -1:
            fixed_pages = fix_update(pages, invalid_index)
            invalid_index = is_update_valid(fixed_pages)

        result += int(pages[len(fixed_pages) // 2])

        line = file.readline().strip()

print("Sum of invalid middle pages:", result)