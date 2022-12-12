import re
import pprint

f = open("input2.txt", "r")
lines = f.readlines()
current_directory = ["/"]
structure = {
    "/": {}
}

for i in range(len(lines)):
    line = lines[i].strip()

    x = re.search(r"^\$ cd \/$", line)
    if x != None:
        current_directory = ["/"]
        print("Change current directory to /")
        continue

    x = re.search(r"^\$ cd ([a-zA-Z]+)$", line)
    if x != None:
        current_directory.append(x.group(1))
        print("Change current directory to", x.group(1))
        continue

    x = re.search(r"^\$ cd \.\.$", line)
    if x != None:
        current_directory.pop()
        print("Change current directory to ..")
        continue

    x = re.search(r"^\$ ls$", line)
    if x != None:
        print("List files and directories contained by current directory")
        continue

    x = re.search(r"^dir ([a-zA-Z]+)$", line)
    if x != None:
        dir = structure
        for d in current_directory:
            dir = dir[d]

        dir[x.group(1)] = {}
        print("Directory", x.group(1), "found")
        continue

    x = re.search(r"^([0-9]+) ([a-zA-Z\.]+)$", line)
    if x != None:
        dir = structure
        for d in current_directory:
            dir = dir[d]

        dir[x.group(2)] = int(x.group(1))
        print("File", x.group(2), "with size of", x.group(1), "bytes found")
        continue

    raise


# Print structure
def print_structure(dir, indent = 0):
    indentation = indent * '  '

    for key in dir:
        if type(dir[key]) is dict:
            print(f"{indentation}- {key} (dir)")
            print_structure(dir[key], indent + 1)
        else:
            print(f"{indentation} - {key} (file, size={dir[key]})")

def calculate_size(dir, indent = 0):
    sum = 0
    indentation = indent * '  '

    for key in dir:
        # print(key, sum)
        if type(dir[key]) is dict:
            print(f"{indentation}- {key} (dir)")
            sum_dir = calculate_size(dir[key], indent + 1)
            sum += sum_dir
        else:
            print(f"{indentation} - {key} (file, size={dir[key]})")
            sum += dir[key]
    
    return sum

def calculate_min_size(dir, indent = 0):
    sum = 0
    indentation = indent * '  '

    for key in dir:
        # print(key, sum)
        if type(dir[key]) is dict:
            print(f"{indentation}- {key} (dir)")
            sum_dir = calculate_min_size(dir[key], indent + 1)
            sum += sum_dir

            global min
            global needed_space
            if sum_dir >= needed_space and sum_dir < min:
                min = sum_dir
        else:
            print(f"{indentation} - {key} (file, size={dir[key]})")
            sum += dir[key]
    
    return sum

# print_structure(structure, 0)
used_space = calculate_size(structure, 0)
free_space = 70000000 - used_space
needed_space = 30000000 - free_space
print(f"Total size used: {used_space}, free: {free_space}, needed: {needed_space}")

min = 70000000
calculate_min_size(structure, 0)
print(f"Minimum size: {min}")