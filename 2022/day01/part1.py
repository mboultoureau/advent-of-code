f = open("input2.txt", "r")
lines = f.readlines()
lines.append("")

sum = 0
max = 0

for line in lines:
    if line.strip() == "":
        if sum > max:
            max = sum
        sum = 0
    else:
        sum += int(line)

print(max)