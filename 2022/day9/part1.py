def displayGrid(top_left_corner, bottom_right_corner, H, T):
    for l in range(top_left_corner[1], bottom_right_corner[1] + 1):
        line = ""
        for c in range(top_left_corner[0], bottom_right_corner[0] + 1):
            if H == (c, l):
                line += "H"
            elif T == (c, l):
                line += "T"
            else:
                line += "."
        print(line)

def displayPositions(top_left_corner, bottom_right_corner, positions):
    for l in range(top_left_corner[1], bottom_right_corner[1] + 1):
        line = ""
        for c in range(top_left_corner[0], bottom_right_corner[0] + 1):
            if (c, l) in positions:
                line += "#"
            else:
                line += "."
        print(line)

def moveH(H, direction):
    if direction == "R":
        H = (H[0] + 1, H[1])
    elif direction == "L":
        H = (H[0] - 1, H[1])
    elif direction == "U":
        H = (H[0], H[1] - 1)
    elif direction == "D":
        H = (H[0], H[1] + 1)
    else:
        raise f"Unknown direction {direction}"

    return H

def moveT(T, H):
    # Check if T touching H ...
    # same position
    if T == H:
        return T

    # vertically
    if H == (T[0], T[1] + 1) or H == (T[0], T[1] - 1):
        return T

    # horizontally
    if H == (T[0] + 1, T[1]) or H == (T[0] - 1, T[1]):
        return T

    # or diagonally
    if (H == (T[0] + 1, T[1] + 1) 
        or H == (T[0] - 1, T[1] + 1)
        or H == (T[0] + 1, T[1] - 1)
        or H == (T[0] - 1, T[1] - 1)):
        return T

    # Move T
    # Same column
    if T[0] == H[0]:
        T = (T[0], T[1] + 1 if H[1] > T[1] else T[1] - 1)

    # Same line
    elif T[1] == H[1]:
        T = (T[0] + 1 if H[0] > T[0] else T[0] - 1, T[1])
    # Diagonal
    elif H[0] > T[0] and H[1] > T[1]:
        T = (T[0] + 1, T[1] + 1)
    elif H[0] > T[0] and H[1] < T[1]:
        T = (T[0] + 1, T[1] - 1)
    elif H[0] < T[0] and H[1] > T[1]:
        T = (T[0] - 1, T[1] + 1)
    elif H[0] < T[0] and H[1] < T[1]:
        T = (T[0] - 1, T[1] - 1)

    return T

def recalculateSize(top_left_corner, bottom_right_corner, H, T):
    # For H
    if H[0] < top_left_corner[0]:
        top_left_corner = (H[0], top_left_corner[1])

    if H[0] > bottom_right_corner[0]:
        bottom_right_corner = (H[0], bottom_right_corner[1])

    if H[1] < top_left_corner[1]:
        top_left_corner = (top_left_corner[0], H[1])

    if H[1] > bottom_right_corner[1]:
        bottom_right_corner = (bottom_right_corner[0], H[1])

    # For T
    if T[0] < top_left_corner[0]:
        top_left_corner = (T[0], top_left_corner[1])

    if T[0] > bottom_right_corner[0]:
        bottom_right_corner = (T[0], bottom_right_corner[1])

    if T[1] < top_left_corner[1]:
        top_left_corner = (top_left_corner[0], T[1])

    if T[1] > bottom_right_corner[1]:
        bottom_right_corner = (bottom_right_corner[0], T[1])

    return (top_left_corner, bottom_right_corner)

def main():
    f = open("input2.txt", "r")
    lines = f.readlines()

    # Positions of H and T
    H = (0, 0)
    T = (0, 0)

    # Coordinates min and max
    top_left_corner = (0, 0)
    bottom_right_corner = (0, 0)

    # Positions visited at least once by tail
    positions = {T}

    print("== Initial State ==\n")
    displayGrid(top_left_corner, bottom_right_corner, H, T)

    for line in lines:
        line = line.strip()
        print(f"\n== {line} ==")

        direction = line.split(" ")[0]
        steps = int(line.split(" ")[1])

        for step in range(steps):
            H = moveH(H, direction)
            T = moveT(T, H)
            (top_left_corner, bottom_right_corner) = recalculateSize(top_left_corner, bottom_right_corner, H, T)
            positions.add(T)

            print("\n")
            displayGrid(top_left_corner, bottom_right_corner, H, T)

    print("\n== POSITIONS ==\n")
    displayPositions(top_left_corner, bottom_right_corner, positions)

    print(f"\n{len(positions)} positions visited by at least once")

if __name__ == "__main__":
    main()
