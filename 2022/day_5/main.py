import os
import errno
import re

crates = [
    "FRW",
    "PWVDCMHT",
    "LNZMP",
    "RHCJ",
    "BTQHGPC",
    "ZFLWCG",
    "CGJZQLVW",
    "CVTWFRNP",
    "VSRGHWJ",
]


def get_top_crates(log=False):
    top_crates = []
    for i, crate in enumerate(crates):
        if log == True:
            print(f"{i+1} - {crate}")
        top_crates.append(crate[0])

    return "".join(top_crates)


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

    # input instructions start from line 10 downwards
    for line in input[10:]:
        # Parse instructions in to a list of numbers [move, from, to]
        instructions = [int(x) for x in re.findall("[0-9]+", line)]
        # Fix instruction 'from' and 'to' indexing
        # instructions = [x - 1 for x in instructions[1:]].insert(0, instructions[0])
        m = instructions[0]  # move
        f = instructions[1] - 1  # from
        t = instructions[2] - 1  # to

        takeout = crates[f][:m]
        reminder = crates[f][m:]

        print(
            f"{line} - {instructions}\nFrom: {crates[f]}\nTake:{takeout}\nReminder:{reminder}\nTo: {crates[t]}\n---"
        )
        crates[f] = reminder

        # Part one solution
        # crates[t] = takeout[::-1] + crates[t]

        # Part two solution
        crates[t] = takeout + crates[t]

    return get_top_crates(log=True)


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

    return "test"


if __name__ == "__main__":
    input = parse("./input.txt")

    part_one_result = solve_part_one(input)
    print(f"Challenge result Part One: {part_one_result}")

    part_two_result = solve_part_two(input)
    print(f"Challenge result Part Two: {part_two_result}")
