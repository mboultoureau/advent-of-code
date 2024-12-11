f = open("input2.txt", "r")
lines = f.readlines()
lines.append("")

total = 0
max = []

for line in lines:
    if line.strip() == "":
        max.append(total)
        max.sort(reverse=True)
        max = max[:3]
        total = 0
    else:
        total += int(line)

print(sum(max))