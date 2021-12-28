f = open("input.txt", "r")
lines = f.readlines()

oxygen_possibilities = []
co2_possibilities = []


# We transform each line in an array
for line in lines:
    line = [int(char) for char in line if char != "\n"]
    oxygen_possibilities.append(line)
    co2_possibilities.append(line)


# OXYGEN

column = 0
while len(oxygen_possibilities) > 1:
    # We count the number of ones in the column
    count = 0
    for possibility in oxygen_possibilities:
        if possibility[column] == 1:
            count = count + 1

    if count >= len(oxygen_possibilities) - count:
        oxygen_possibilities = list(filter(lambda x: (x[column] == 1), oxygen_possibilities))
    else:
        oxygen_possibilities = list(filter(lambda x: (x[column] == 0), oxygen_possibilities))

    column = column + 1

# CO2

column = 0
while len(co2_possibilities) > 1:
    # We count the number of ones in the column
    count = 0
    for possibility in co2_possibilities:
        if possibility[column] == 1:
            count = count + 1
    
    if count < len(co2_possibilities) - count:
        co2_possibilities = list(filter(lambda x: (x[column] == 1), co2_possibilities))
    else:
        co2_possibilities = list(filter(lambda x: (x[column] == 0), co2_possibilities))

    column = column + 1

# We convert int array in string
oxygen =  [str(i) for i in oxygen_possibilities[0]]
co2 =  [str(i) for i in co2_possibilities[0]]

# We convert binary to decimal
oxygen_decimal = int(''.join(oxygen), 2)
co2_decimal = int(''.join(co2), 2)

print(f"Oxygen: {oxygen} ({oxygen_decimal})")
print(f"CO2: {co2} ({co2_decimal})")

print(f"Result: {oxygen_decimal * co2_decimal}")