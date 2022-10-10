f = open("input.txt", "r")
lines = f.readlines()

nb_of_grid = int((len(lines) - 1) / 6)
print(f"Number of grid : {nb_of_grid}")

numbers = lines[0].strip().split(",")
print(f"Numbers : {numbers}")

class Grid:
    id = 0
    numbers = []
    checked = []

    def __init__(self, lines, id = 0) -> None:
        # Init  5x5 checked matrix with False
        self.checked = [[False for _ in range(5)] for _ in range(5)]

        # Init 5x5 numbers matrix with lines
        self.numbers = []
        for line in lines:
            self.numbers.append([int(x) for x in list(filter(lambda n: n != "", line.strip().split(" ")))])

        self.id = id

    def check_number(self, n) -> None:
        x = -1
        y = -1
        for i, e in enumerate(self.numbers):
            try:
                y = e.index(n)
                x = i
            except ValueError:
                pass
        
        if x != -1:
            self.checked[x][y] = True

    def check_victory(self) -> bool:
        for i in range(5):
            if self.checked[i][0] == self.checked[i][1] == self.checked[i][2] == self.checked[i][3] == self.checked[i][4] == True:
                return True

            if self.checked[0][i] == self.checked[1][i] == self.checked[2][i] == self.checked[3][i] == self.checked[4][i] == True:
                return True

        return False
        
    def debug(self) -> None:
        print(f"--- Grille {self.id} ---")
        print(f"Checked: {self.checked}")
        print(f"Numbers: {self.numbers}\n")

    def calculate_score(self, n) -> None:
        score = 0
        for i in range(5):
            for j in range(5):
                if self.checked[i][j] == False:
                    score += self.numbers[i][j]
            
        return score * n

grids = []

# Initialization of grids
for i in range(nb_of_grid):
    grid = Grid(lines[i * 6 + 2:i * 6 + 7], i)
    grid.debug()
    grids.append(grid)

# For each number
for n in numbers:
    for grid in grids:
        grid.check_number(int(n))
        if grid.check_victory():
            print(f"Answer: {grid.calculate_score(int(n))}")
            exit()
