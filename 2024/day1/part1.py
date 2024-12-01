distance = 0
list1 = []
list2 = []

with open('./input.txt') as file:
    line = file.readline()
    while line:
        parts = line.strip().split('   ')
        list1.append(int(parts[0]))
        list2.append(int(parts[1]))
        line = file.readline()

list1.sort()
list2.sort()

for i in range(len(list1)):
    distance += abs(list1[i] - list2[i])

print("Total distance:", distance)