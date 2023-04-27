import os
import errno


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

    stream = input[0]
    marker_positions = []
    marker_size = 14

    for i in range(0, len(stream)):
        if i + 4 <= len(stream):
            marker_check = stream[i : i + marker_size]
            if len(set(marker_check)) == len(marker_check):
                marker_positions.append(i + marker_size)
                print(f"{marker_check} - {i + marker_size}")
            # print(f"{marker_check} - {set(marker_check)}-{len(marker_check)}")
    return len(stream)


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
    input = parse("./input.txt")

    part_one_result = solve_part_one(input)
    part_two_result = solve_part_two(input)
    print(
        f"\nChallenge result Part One: {part_one_result}\nChallenge result Part Two: {part_two_result}"
    )
