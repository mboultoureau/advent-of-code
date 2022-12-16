import re
import math

class Monkey:
    id = 0
    starting_items: None
    operation_operator = ''
    operation_value = ''
    test_divisible = 0
    true_throw = 0
    false_throw = 0
    inspection = 0

    def print(self):
        print(f"=== Monkey {self.id} ===")
        print(f"Starting items: {self.starting_items}")
        print(f"Operation: old {self.operation_operator} {self.operation_value}")
        print(f"Test: divisible by {self.test_divisible}")
        print(f"  If true: throw to monkey {self.true_throw}")
        print(f"  If false: throw to monkey {self.false_throw}")

def parse_file(filename):
    f = open(filename, "r")
    lines = f.readlines()

    monkeys = []

    i = 0
    while i < len(lines):
        monkey = Monkey()

        # Monkey ID
        line = lines[i].strip()
        x = re.search(r"^Monkey ([0-9]+):$", line)
        monkey.id = x.group(1)
        i += 1

        # Starting items
        line = lines[i].strip()
        x = re.findall(r"[0-9]+", line)
        monkey.starting_items = x
        i += 1

        # Operation
        line = lines[i].strip()
        x = re.search(r"^Operation: new = old ([*+]) ([0-9]+|old)$", line)
        monkey.operation_operator = x.group(1)
        monkey.operation_value = x.group(2)
        i += 1

        # Test
        line = lines[i].strip()
        x = re.search(r"^Test: divisible by ([0-9]+)$", line)
        monkey.test_divisible = int(x.group(1))
        i += 1

        # True
        line = lines[i].strip()
        x = re.search(r"^If true: throw to monkey ([0-9]+)$", line)
        monkey.true_throw = int(x.group(1))
        i += 1

        # False
        line = lines[i].strip()
        x = re.search(r"^If false: throw to monkey ([0-9]+)$", line)
        monkey.false_throw = int(x.group(1))
        i += 2

        monkeys.append(monkey)

    return monkeys

def process_one_monkey(monkeys, monkeyId, divisor):
    
    monkey = monkeys[monkeyId]

    # print(f"Monkey {monkey.id}:")

    for item in monkey.starting_items:
        # Worry level
        worry_level = int(item)
        monkey.inspection += 1
        # print(f"  Monkey inspects an item with a worry level of {worry_level}.")

        # Operation
        if monkey.operation_operator == '+' and monkey.operation_value == 'old':
            worry_level += worry_level
        elif monkey.operation_operator == '*' and monkey.operation_value == 'old':
            worry_level *= worry_level
        elif monkey.operation_operator == '+':
            worry_level += int(monkey.operation_value)
        elif monkey.operation_operator == '*':
            worry_level *= int(monkey.operation_value)
        else:
            raise "Unknow operator"

        # print(f"    New worry level: {worry_level}")

        # # Divided by 3
        worry_level = worry_level % divisor

        # print(f"    Divided by 3: {worry_level}")

        # Divisible ?
        if worry_level % monkey.test_divisible == 0:
            # print(f"    Current worry level is divisible by {monkey.test_divisible}.")
            monkeys[monkey.true_throw].starting_items.append(worry_level)
        else:
            # print(f"    Current worry level is not divisible by {monkey.test_divisible}.")
            monkeys[monkey.false_throw].starting_items.append(worry_level)

    monkey.starting_items = []

    return monkeys

def print_holding_items(monkeys):
    for monkey in monkeys:
        print(f"Monkey {monkey.id}: {monkey.starting_items}")

def print_inspections(monkeys):
    for monkey in monkeys:
        print(f"Monkey {monkey.id} nspected items {monkey.inspection} times")

def calculate_divisor(monkeys):
    divisor = 1
    for monkey in monkeys:
        divisor *= monkey.test_divisible
    
    return divisor


def main():
    monkeys = parse_file("input2.txt")
    monkey_divisor = calculate_divisor(monkeys)

    print(monkey_divisor)
    for j in range(10000):
        for i in range(len(monkeys)):
            monkeys = process_one_monkey(monkeys, i, monkey_divisor)

    # print_holding_items(monkeys)
    print_inspections(monkeys)

    inspections = []
    for monkey in monkeys:
        inspections.append(monkey.inspection)

    inspections.sort(reverse=True)
    print(f"Result: {inspections[0] * inspections[1]}")

if __name__ == "__main__":
    main()