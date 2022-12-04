f = open("input2.txt", "r")
lines = f.readlines()
total_priority = 0
nb_lines = len(lines)

for i in range(0, nb_lines, 3):
    common_letter = ''.join(set(lines[i].strip())
        .intersection(lines[i + 1].strip())
        .intersection(lines[i + 2].strip()))
    
    priority = 0

    # Calculate priority
    if ord(common_letter) >= 97 and ord(common_letter) <= 122:
        priority = ord(common_letter) - 96
    elif ord(common_letter) >= 65 and ord(common_letter) <= 90:
        priority = ord(common_letter) - 64 + 26

    total_priority += priority

print("Total priority:", total_priority)