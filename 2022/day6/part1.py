f = open("input2.txt", "r")
lines = f.readlines()

for line in lines:
    line = line.strip()
    for i in range(3, len(line)):
        if len({line[i - 3], line[i - 2], line[i - 1], line[i]}) == 4:
            break
    print(i + 1)