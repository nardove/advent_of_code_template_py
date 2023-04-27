def parse(path_to_file):
    """Parse input file into a list

    Args:
        path_to_file (str): path to input file
    """
    with open(path_to_file, "r") as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


scores = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def solve_part_one(input):
    """Given an list solve [Day 3 challenge](https://adventofcode.com/2022/day/3)

    Args:
        input (list): list of values from parsed input file

    Raises:
        TypeError: Missing input argument

    Returns:
        int: score
    """
    if input == None or len(input) == 0:
        raise TypeError("Missing input argument or empty list")

    total = 0
    for rucksack in input:
        middle = len(rucksack) // 2
        compartment1 = rucksack[:middle]
        compartment2 = rucksack[middle:]

        for char in compartment2:
            if char in compartment1:
                total += scores.index(char) + 1
                break

    return total


def solve_part_two(input):
    """Given an input list solve second part of the puzzle

    Args:
        input (list): list of inputs
    """
    if input == None or len(input) == 0:
        raise TypeError("Missing input argument or empty list")

    total = 0
    for group in range(0, len(input) - 1, 3):
        group1 = input[group]
        group2 = input[group + 1]
        group3 = input[group + 2]

        for char in group1:
            if char in group2 and char in group3:
                total += scores.index(char) + 1
                break

    return total


if __name__ == "__main__":

    input = parse("./input.txt")

    part_one_result = solve_part_one(input)
    print(f"Result Day3 Challenge Part One: {part_one_result}")

    part_two_result = solve_part_two(input)
    print(f"Result Day3 Challenge Part Two: {part_two_result}")
