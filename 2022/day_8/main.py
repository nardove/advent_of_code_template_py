import os
import errno
import sys
from colorama import Fore, Style

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
    cols = len(input[0])
    rows = len(input)
    visible_trees = 0
    grid = []
    scores = []

    debug = False
    for line in input:
        grid.append(list(line))
        if debug:
            print(line)
    print('')

    for i, line in enumerate(input[1:-1]):
        for j, _ in enumerate(line[1:-1]):
            row = grid[i+1:i+2][0]
            col = [row[j+1] for row in grid]
            tree = grid[i+1][j+1]
            left = col[:i+1]
            right = col[i+2:]
            up = row[:j+1]
            down = row[j+2:]
            
            if tree > max(left) or tree > max(right) or tree > max(up) or tree > max(down):
                visible_trees += 1

            # print(f"{Style.RESET_ALL}r: {Fore.YELLOW}{row}{Style.RESET_ALL} - c: {Fore.CYAN}{col}{Style.RESET_ALL} - t: {Fore.BLUE}{tree}{Style.RESET_ALL} - {Fore.CYAN}{i+1},{Fore.YELLOW}{j+1}{Style.RESET_ALL} - {visible_trees}")

    return visible_trees + (rows + cols - 2) * 2 


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

    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 's':
        input = parse("./sample.txt")
    else:
        input = parse("./input.txt")
    
    part_one_result = solve_part_one(input)
    print(f"\nChallenge result Part One: {part_one_result}")

    part_two_result = solve_part_two(input)
    print(f"Challenge result Part Two: {part_two_result}")
