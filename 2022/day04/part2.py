import re

f = open("input2.txt", "r")
lines = f.readlines()
nb_invalid = 0

for line in lines:
    match = re.search(r"([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)", line)
    elf1_start = int(match.group(1))
    elf1_end = int(match.group(2))
    elf2_start = int(match.group(3))
    elf2_end = int(match.group(4))

    # Check pairs that overlap at all
    if elf1_start <= elf2_start <= elf1_end or elf2_start <= elf1_start <= elf2_end:
        nb_invalid += 1
    
print("Number of invalid assignments:", nb_invalid)