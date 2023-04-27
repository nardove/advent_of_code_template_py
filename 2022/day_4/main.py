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


def get_min_max(section):
    """Given a string in the form "0-9" returns the minimum and maximun values

    Args:
        section (str): String with lower and upper bound range e.g.: "0-9"

    Returns:
        tuple: tuple with min and max values as integers
    """
    a = section.split("-")[0]
    b = section.split("-")[1]
    return (int(a), int(b) + 1)


def solve_part_one(input):
    """Given a input list return the part one challenge result

    Args:
        input (list): Input list of values

    Returns:
        int: part one challenge result
    """
    if input == None or len(input) == 0:
        raise TypeError("Missing input argument or empty list")

    total = 0
    for line in input:
        sections = line.split(",")

        section_1 = get_min_max(sections[0])
        section_2 = get_min_max(sections[1])

        sec_1_min = min(section_1)
        sec_1_max = max(section_1)
        sec_2_min = min(section_2)
        sec_2_max = max(section_2)

        # Check if section 1 is inside section 2
        if (
            sec_1_min >= sec_2_min
            and sec_1_max <= sec_2_max
            or sec_2_min >= sec_1_min
            and sec_2_max <= sec_1_max
        ):
            total += 1

        # print(f"{section_1} min: {sec_1_min}, max: {sec_1_max}")
        # print(f"{section_2} min: {sec_2_min}, max: {sec_2_max}\n")

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

    total = 0
    for line in input:
        sections = line.split(",")

        section_1 = get_min_max(sections[0])
        section_2 = get_min_max(sections[1])

        list_1 = [item for item in range(min(section_1), max(section_1))]
        list_2 = [item for item in range(min(section_2), max(section_2))]

        overlap = [value for value in list_1 if value in list_2]

        if len(overlap) > 0:
            total += 1

    return total


if __name__ == "__main__":
    input = parse("./input.txt")

    part_one_result = solve_part_one(input)
    print(f"Challenge result Part One: {part_one_result}")

    part_two_result = solve_part_two(input)
    print(f"Challenge result Part Two: {part_two_result}")
