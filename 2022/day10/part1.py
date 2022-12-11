import re

def check_if_signal(cycles, register):
    if cycles in [20, 60, 100, 140, 180, 220]:
        print(cycles, register)
        return cycles * register

    return 0

def main():
    f = open("input2.txt", "r")
    lines = f.readlines()

    cycles = 1
    register = 1

    sum = 0

    for line in lines:
        x = re.search(r"addx ([-0-9]+)", line.strip())
        if x != None:
            cycles += 1
            sum += check_if_signal(cycles, register)
            cycles += 1
            register += int(x.group(1))
            sum += check_if_signal(cycles, register)
        else:
            cycles += 1
            sum += check_if_signal(cycles, register)

    print(f"Sum: {sum}")
        

if __name__ == "__main__":
    main()