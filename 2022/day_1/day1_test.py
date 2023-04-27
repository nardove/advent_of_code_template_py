from day1 import *


def test_parse_returns_a_list():
    parsed_input = parse("./input.txt")

    assert isinstance(parsed_input, list)


def test_solve_function_retunrs_an_int():
    solution = solve(
        [
            "10",
            "20",
            "30",
        ]
    )

    assert isinstance(solution, int)
