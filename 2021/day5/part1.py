import re

f = open("input.txt", "r")
lines = f.readlines()

def print_matrix(matrix):
    for row in matrix:
        print(row)

class Segment:
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def debug(self):
        print(f"(x1, y1) = ({self.x1}, {self.y1})")
        print(f"(x2, y2) = ({self.x2}, {self.y2})\n")

segments = []
height = 0
width = 0

for line in lines:
    result = re.search(r"(\d+),(\d+) -> (\d+),(\d+)", line)
    segment = Segment(int(result.group(1)), int(result.group(2)), int(result.group(3)), int(result.group(4)))
    segments.append(segment)

    if max([int(result.group(1)), int(result.group(3))]) > width:
        width = max([int(result.group(1)), int(result.group(3))])
    
    if max([int(result.group(2)), int(result.group(4))]) > height:
        height = max([int(result.group(2)), int(result.group(4))])

height = height + 1
width = width + 1
matrix = [[0 for x in range(width)] for y in range(height)]

print(f"Height: {height} - Width: {width}")

for segment in segments:
    if segment.x1 == segment.x2:
        begin = min([segment.y1, segment.y2])
        length = max([segment.y1, segment.y2]) - min([segment.y1, segment.y2]) + 1

        for i in range(length):
            matrix[begin + i][segment.x1] = matrix[begin + i][segment.x1] + 1
    elif segment.y1 == segment.y2:
        begin = min([segment.x1, segment.x2])
        length = max([segment.x1, segment.x2]) - min([segment.x1, segment.x2]) + 1

        for i in range(length):
            matrix[segment.y1][begin + i] = matrix[segment.y1][begin + i] + 1

score = 0
for row in range(height):
    for col in range(width):
        if matrix[row][col] >= 2:
            score = score + 1

print_matrix(matrix)
print(score)
