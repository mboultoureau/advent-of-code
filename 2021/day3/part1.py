f = open("input.txt", "r")
lines = f.readlines()

number_of_lines = len(lines)
number_of_caracters = len(lines[0]) - 1

# Ex : [0, 0, 0, 0, 0]
gamma = [0] * number_of_caracters

# We add each number of each line to get the number of 1 per column
for line in lines:
    a = [int(char) for char in line if char != "\n"]
    gamma = [gamma[i] + a[i] for i in range(len(a))]

# We check the number of ones per column to see if there are more ones than zeros
for index, val in enumerate(gamma):
    if val > int(number_of_lines / 2):
        gamma[index] = 1
    else:
        gamma[index] = 0

# Epsilon rate is the opposite of gamma rate
epsilon = [1 if i == 0 else 0 for i in gamma]

# We convert int array in string
gamma =  [str(i) for i in gamma]
epsilon =  [str(i) for i in epsilon]

# We convert binary to decimal
gamma_decimal = int(''.join(gamma), 2)
epsilon_decimal = int(''.join(epsilon), 2)

print(f"Gamma: {gamma} ({gamma_decimal})")
print(f"Epsilon: {epsilon} ({epsilon_decimal})")

print(f"Result: {gamma_decimal * epsilon_decimal}")