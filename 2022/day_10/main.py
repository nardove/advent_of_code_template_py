import os
import errno
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
    signals = [0]
    X = 1

    for line in input:
        if line[:4] == "noop":
            signals.append(X)
        else:
            signals.append(X)
            signals.append(X)
            X += int(line[4:])

    signals.append(X)

    return sum([x * y for x, y in list(enumerate(signals))[20::40]])


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
    signals = []
    X = 1

    for line in input:
        if line[:4] == "noop":
            signals.append(X)
        else:
            signals.append(X)
            signals.append(X)
            X += int(line[4:])

    for i in range(0, len(signals), 40):
        for j in range(40):
            print("#" if abs(signals[i + j] - j) <= 1 else " ", end="")
        print()

    return 0


if __name__ == "__main__":
    input = parse("input.txt")

    part_one_result = solve_part_one(input)
    print(f"Challenge result Part One: {Fore.LIGHTCYAN_EX}{part_one_result}")

    print(Style.RESET_ALL)

    part_two_result = solve_part_two(input)
    print(f"Challenge result Part Two: {Fore.MAGENTA}{part_two_result}")
