def parse(puzzle_input):
    """Parse input file

    Args:
        puzzle_input (str): path to the input file
    """
    with open(puzzle_input, "r") as f:
        lines = f.readlines()

    return lines


def solve(input):
    """Solve function for the given input

    Args:
        input (list): input list of strings
    """

    totals = []
    count = 0

    for index, line in enumerate(input):
        if line == "\n" or index == len(input) - 1:
            totals.append(count)
            count = 0
        else:
            count += int(line)

    totals.sort(reverse=True)
    print(sum(totals[:3]))

    return max(totals)


if __name__ == "__main__":
    input = parse("./input.txt")
    
    print(f"Solution: {solve(input)}")
