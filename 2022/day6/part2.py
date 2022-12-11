f = open("input2.txt", "r")
lines = f.readlines()

for line in lines:
    line = line.strip()
    for i in range(14, len(line)):
        if len(set(list(line[i-14:i]))) == 14:
            break
    print(i)