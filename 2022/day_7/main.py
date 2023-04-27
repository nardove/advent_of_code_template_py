import os
import errno
import re


path = "/home"
dirs = { path: 0 }


def parse(input):
    """Parse given input file and retuns a list for each line in the document

    Args:
        input (str): Path to the input.txt file

    Raises:
        FileNotFoundError: Input file path not found

    Returns:
        list: parsed
    """

    if not os.path.exists(input):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), input)

    with open(input, "r") as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def solve_part_one(input):
    """Given a input list return the part one challenge result

    Args:
        input (list): Input list of values

    Returns:
        int: part one challenge result
    """
    if input == None or len(input) == 0:
        raise TypeError("Missing input argument or empty list")

    # Part one challenge logic goes here
    # Pocess every command
    for line in input:
        match line[0:4]:
            # Handle commands
            case '$ cd':
                dir = line[5:]
            
                match dir:
                    case '/':
                        path = "/home"
                        
                    case '..':
                        # Goes back 1 dir up
                        path = path[:path.rfind("/")]
                
                    case _:
                        # Creates a path and adds them to dirs dict
                        path = path + '/' + dir
                        dirs.update({ path: 0 })
            
            # Handle files in directory
            case _:
                # Check for file sizes
                bites = re.findall("[0-9]+", line)
                dir = path
                
                # If a file is found
                # Add the total file size count to its corresponding dir/path
                if len(bites) > 0:
                    for _ in range(path.count('/')):
                        dirs[dir] += int(bites[0])
                        dir = dir[:dir.rfind('/')]

    total = 0
    for dir in dirs:
        # print(dir, dirs[dir])
        
        if dirs[dir] <= 1e5:
            total += dirs[dir]

    return total


def solve_part_two(input):
    """Given a input list return the part two challenge result

    Args:
        input (list): Input list of values

    Returns:
        int: part two challenge result
    """
    if input == None or len(input) == 0:
        raise TypeError("Missing input argument or empty list")

    # Part two challenge logic goes here
    smallest_dir_size = []
    total_space = int(7e7)
    min_space = int(3e7)
    total_dirs_space = list(dirs.values())[0]
    min_space_to_delete = min_space - (total_space - total_dirs_space)

    for dir in dirs:
        if (dirs[dir] >= min_space_to_delete):
            smallest_dir_size.append(dirs[dir])

    return min(smallest_dir_size)


if __name__ == "__main__":
    input = parse("./input.txt")

    part_one_result = solve_part_one(input)
    print(f"Challenge result Part One: {part_one_result}")

    part_two_result = solve_part_two(input)
    print(f"Challenge result Part Two: {part_two_result}")
