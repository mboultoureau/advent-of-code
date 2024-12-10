from collections import Counter

similarity = 0
list1 = []
list2 = []

with open('./input.txt') as file:
    line = file.readline()
    while line:
        parts = line.strip().split('   ')
        list1.append(int(parts[0]))
        list2.append(int(parts[1]))
        line = file.readline()

list2 = Counter(list2)

for n in list1:
    similarity += list2[n] * n

print("Similarity score:", similarity)