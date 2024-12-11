f = open("input2.txt", "r")
lines = f.readlines()
total_priority = 0

for line in lines:
    line = line.strip()
    first_compartment = line[0:len(line) // 2]
    second_compartment = line[len(line) // 2:len(line)]

    common_letter = ''.join(set(first_compartment).intersection(second_compartment))
    priority = 0

    # Calculate priority
    if ord(common_letter) >= 97 and ord(common_letter) <= 122:
        priority = ord(common_letter) - 96
    elif ord(common_letter) >= 65 and ord(common_letter) <= 90:
        priority = ord(common_letter) - 64 + 26

    total_priority += priority

print("Total priority:", total_priority)