from collections import deque
from enum import Flag, auto
import os

class FenceDirection(Flag):
    LEFT = auto()
    RIGHT = auto()
    TOP = auto()
    BOTTOM = auto()

def read_file(filename):
    directory_path = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(directory_path, filename)
    
    garden = []
    with open(input_path) as file:
        for line in file:
            garden.append(list(line.strip()))

    return garden

# PART 1
def calculate_fence(garden):
    total_price = 0
    visited = set()

    NB_ROWS = len(garden)
    NB_COLS = len(garden[0])

    for row in range(NB_ROWS):
        for col in range(NB_COLS):
            area = 0
            perimeter = 0
            queue = deque([(row, col, )])

            while queue:
                r, c = queue.popleft()
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                if (r, c) in visited:
                    continue

                if r < 0 or r >= NB_ROWS or c < 0 or c >= NB_COLS:
                    continue

                if garden[row][col] != garden[r][c]:
                    continue

                area += 1
                if r - 1 < 0 or garden[r - 1][c] != garden[r][c]:
                    perimeter += 1
                if r + 1 >= NB_ROWS or garden[r + 1][c] != garden[r][c]:
                    perimeter += 1
                if c - 1 < 0 or garden[r][c - 1] != garden[r][c]:
                    perimeter += 1
                if c + 1 >= NB_COLS or garden[r][c + 1] != garden[r][c]:
                    perimeter += 1

                visited.add((r, c))

                for dr, dc in directions:
                    queue.append((r + dr, c + dc))

            total_price += area * perimeter

    return total_price

# PART 2
def calculate_fence_with_discount(garden):
    total_price = 0
    visited = set()

    NB_ROWS = len(garden)
    NB_COLS = len(garden[0])

    fence_map = [[FenceDirection(0) for _ in range(NB_COLS)] for _ in range(NB_ROWS)]

    # Build fence map
    for row in range(NB_ROWS):
        for col in range(NB_COLS):
            queue = deque([(row, col)])

            while queue:
                r, c = queue.popleft()
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                if (r, c) in visited:
                    continue

                if r < 0 or r >= NB_ROWS or c < 0 or c >= NB_COLS:
                    continue

                if garden[row][col] != garden[r][c]:
                    continue

                fence = FenceDirection(0)
                if r - 1 < 0 or garden[r - 1][c] != garden[r][c]:
                    fence |= FenceDirection.TOP
                    
                if r + 1 >= NB_ROWS or garden[r + 1][c] != garden[r][c]:
                    fence |= FenceDirection.BOTTOM

                if c - 1 < 0 or garden[r][c - 1] != garden[r][c]:
                    fence |= FenceDirection.LEFT

                if c + 1 >= NB_COLS or garden[r][c + 1] != garden[r][c]:
                    fence |= FenceDirection.RIGHT

                fence_map[r][c] = fence
                visited.add((r, c))

                for dr, dc in directions:
                    queue.append((r + dr, c + dc))

    visited = set()
    for row in range(NB_ROWS):
        for col in range(NB_COLS):
            area = 0
            perimeter = 0
            queue = deque([(row, col)])

            while queue:
                r, c = queue.popleft()
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                if (r, c) in visited:
                    continue

                if r < 0 or r >= NB_ROWS or c < 0 or c >= NB_COLS:
                    continue

                if garden[row][col] != garden[r][c]:
                    continue

                area += 1
                if FenceDirection.TOP in fence_map[r][c] and (c == 0 or garden[r][c] != garden[r][c - 1] or FenceDirection.TOP not in fence_map[r][c - 1]):
                    perimeter += 1
                if FenceDirection.BOTTOM in fence_map[r][c] and (c == 0 or garden[r][c] != garden[r][c - 1] or FenceDirection.BOTTOM not in fence_map[r][c - 1]):
                    perimeter += 1
                if FenceDirection.LEFT in fence_map[r][c] and (r == 0 or garden[r][c] != garden[r - 1][c] or FenceDirection.LEFT not in fence_map[r - 1][c]):
                    perimeter += 1
                if FenceDirection.RIGHT in fence_map[r][c] and (r == 0 or garden[r][c] != garden[r - 1][c] or FenceDirection.RIGHT not in fence_map[r - 1][c]):
                    perimeter += 1

                visited.add((r, c))

                for dr, dc in directions:
                    queue.append((r + dr, c + dc))

            total_price += area * perimeter

    return total_price

if __name__ == "__main__":
    garden = read_file('input.txt')
    price = calculate_fence(garden)
    print("[PART 1] Total price:", price)

    price = calculate_fence_with_discount(garden)
    print("[PART 2] Total price:", price)