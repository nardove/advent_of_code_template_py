import os
import errno
from colorama import Fore, Back, Style


def parse(input):
    if not os.path.exists(input):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), input)

    with open(input, "r") as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def solve_part_one(input):
    if input == None or len(input) == 0:
        raise TypeError("Missing input argument or empty list")

    floor = 0
    for c in input[0]:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        else:
            raise ValueError("Invalid character in input")

    return floor


def solve_part_two(input):
    if input == None or len(input) == 0:
        raise TypeError("Missing input argument or empty list")

    floor = 0
    for i, c in enumerate(input[0]):
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        else:
            raise ValueError("Invalid character in input")

        if floor == -1:
            return i + 1


if __name__ == "__main__":
    input = parse("input.txt")
    print(input)
    part_one_result = solve_part_one(input)
    print(f"Challenge result Part One: {Fore.LIGHTCYAN_EX}{part_one_result}")

    print(Style.RESET_ALL)

    part_two_result = solve_part_two(input)
    print(f"Challenge result Part Two: {Fore.MAGENTA}{part_two_result}")
