def parse(path_to_file):
    """Parse input file into a list

    Args:
        path_to_file (str): path to the input file
    """
    with open(path_to_file, "r") as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def solve(input):
    """Given an list solve [Day 2 challenge](https://adventofcode.com/2022/day/2)

    Args:
        input (list): list of values from parsed input file

    Raises:
        TypeError: Missing input argument

    Returns:
        int: score
    """
    if input == None or len(input) == 0:
        raise TypeError("Missing input argument or empty list")

    # choosen_score = {"X": 1, "Y": 2, "Z": 3}
    choosen_score = {"A": 1, "B": 2, "C": 3}
    total_scores = []
    result = ""

    for pair in input:
        points = 0
        match_score = 0
        match_result = pair[-1]
        oponent_hand = pair[0]

        # match pair:
        #     case "A Z" | "C Y" | "B X":
        #         result = "lost"
        #         points = 0
        #     case "A X" | "B Y" | "C Z":
        #         result = "draw"
        #         points = 3
        #     case _:
        #         result = "win"
        #         points = 6

        match match_result:
            case "X":
                result = "lost"
                points = 0
                match oponent_hand:
                    case "A":
                        hand = "C"
                    case "C":
                        hand = "B"
                    case _:
                        hand = "A"
            case "Y":
                result = "draw"
                points = 3
                hand = oponent_hand
            case _:
                result = "win"
                points = 6
                match oponent_hand:
                    case "A":
                        hand = "B"
                    case "C":
                        hand = "A"
                    case _:
                        hand = "C"

        match_score = points + choosen_score[hand]
        total_scores.append(match_score)
        print(f"{pair} - {hand} - {result} - {match_score}")

    return sum(total_scores)


if __name__ == "__main__":

    input = parse("./input.txt")

    result = solve(input)
    print(f"Result Day2 Challenge:  {result}")
