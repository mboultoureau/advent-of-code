import os

total = 0

directory_path = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(directory_path, "input.txt")

def is_valid(target, values, current, index):
    if index == len(values):
        return current == target
    
    if is_valid(target, values, current + values[index], index + 1):
        return True

    if is_valid(target, values, current * values[index], index + 1):
        return True

    if is_valid(target, values, int(str(current) + str(values[index])), index + 1):
        return True

    return False

with open(input_path) as file:
    line = file.readline()

    while line:
        target, values = line.strip().split(': ')
        target = int(target)
        values = [int(v) for v in values.split(' ')]

        if is_valid(target, values, values[0], 1):
            total += target
        
        line = file.readline()

print('Total calibration result:', total)