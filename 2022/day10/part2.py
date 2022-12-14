import re

def check_if_signal(cycles, register):
    if cycles in [20, 60, 100, 140, 180, 220]:
        print(cycles, register)
        return cycles * register

    return 0

def display(pixels):
    for y in range(6):
        row = f"Cycle  {y * 40 + 1}\t--> "
        for x in range(40):
            if pixels[y * 40 + x] == True:
                row += '#'
            else:
                row += '.'
        row += f' <-- \t Cycle\t{(y + 1) * 40}'
        print(row)


def main():
    f = open("input2.txt", "r")
    lines = f.readlines()
    pixels = [False] * 240

    display(pixels)

    cycles = 0
    register = 1

    sum = 0

    for line in lines:
        x = re.search(r"addx ([-0-9]+)", line.strip())
        if x != None:
            if cycles % 40 == register or cycles % 40 == register - 1 or cycles % 40 == register + 1:
                pixels[cycles] = True
            cycles += 1
            sum += check_if_signal(cycles, register)

            if cycles % 40 == register or cycles % 40 == register - 1 or cycles % 40 == register + 1:
                pixels[cycles] = True
            cycles += 1
            register += int(x.group(1))
            sum += check_if_signal(cycles, register)
        else:
            if cycles % 40 == register or cycles % 40 == register - 1 or cycles % 40 == register + 1:
                pixels[cycles] = True
            cycles += 1
            sum += check_if_signal(cycles, register)

    print(f"Sum: {sum}")

    display(pixels)
        

if __name__ == "__main__":
    main()