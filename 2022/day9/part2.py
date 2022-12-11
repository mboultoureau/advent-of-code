def displayGrid(top_left_corner, bottom_right_corner, H, knots):
    for l in range(top_left_corner[1], bottom_right_corner[1] + 1):
        line = ""
        for c in range(top_left_corner[0], bottom_right_corner[0] + 1):
            if H == (c, l):
                line += "H"
            else:
                found = "."
                for i in range(len(knots)):
                    if knots[i] == (c, l):
                        found = str(i + 1)
                        break
                
                line += found
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

def moveKnots(knots, H):
    previous = H

    print(f"H: {H}")

    for i in range(len(knots)):
        T = knots[i]

        # Check if knot touching the previous one ...
        # same position
        if T == previous:
            previous = T
            continue

        # vertically
        if previous == (T[0], T[1] + 1) or previous == (T[0], T[1] - 1):
            previous = T
            continue

        # horizontally
        if previous == (T[0] + 1, T[1]) or previous == (T[0] - 1, T[1]):
            previous = T
            continue

        # or diagonally
        if (previous == (T[0] + 1, T[1] + 1) 
            or previous == (T[0] - 1, T[1] + 1)
            or previous == (T[0] + 1, T[1] - 1)
            or previous == (T[0] - 1, T[1] - 1)):
            previous = T
            continue

        # Move T
        # Same column
        if T[0] == previous[0]:
            knots[i] = (T[0], T[1] + 1 if previous[1] > T[1] else T[1] - 1)

        # Same line
        elif T[1] == previous[1]:
            knots[i] = (T[0] + 1 if previous[0] > T[0] else T[0] - 1, T[1])
        # Diagonal
        elif previous[0] > T[0] and previous[1] > T[1]:
            knots[i] = (T[0] + 1, T[1] + 1)
        elif previous[0] > T[0] and previous[1] < T[1]:
            knots[i] = (T[0] + 1, T[1] - 1)
        elif previous[0] < T[0] and previous[1] > T[1]:
            knots[i] = (T[0] - 1, T[1] + 1)
        elif previous[0] < T[0] and previous[1] < T[1]:
            knots[i] = (T[0] - 1, T[1] - 1)

        previous = knots[i]

    return knots

def recalculateSize(top_left_corner, bottom_right_corner, H, knots):
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
    for T in knots:
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
    knots = []

    for i in range(9):
        knots.append((0, 0))

    # Coordinates min and max
    top_left_corner = (0, 0)
    bottom_right_corner = (0, 0)

    # Positions visited at least once by tail
    positions = {(0, 0)}

    print("== Initial State ==\n")
    displayGrid(top_left_corner, bottom_right_corner, H, knots)

    for line in lines:
        line = line.strip()
        print(f"\n== {line} ==")

        direction = line.split(" ")[0]
        steps = int(line.split(" ")[1])

        for step in range(steps):
            H = moveH(H, direction)
            knots = moveKnots(knots, H)
            (top_left_corner, bottom_right_corner) = recalculateSize(top_left_corner, bottom_right_corner, H, knots)


            positions.add(knots[8])

            print("\n")
            displayGrid(top_left_corner, bottom_right_corner, H, knots)

    print("\n== POSITIONS ==\n")
    displayPositions(top_left_corner, bottom_right_corner, positions)

    print(f"\n{len(positions)} positions visited by at least once")

if __name__ == "__main__":
    main()
