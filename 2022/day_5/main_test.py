from main import *
import pytest


def test_parse_input_function_as_an_argument():
    with pytest.raises(FileNotFoundError):
        parse("./input.csv")


def test_parse_input_function_returns_a_list():
    parsed = parse("./input.txt")
    assert isinstance(parsed, list)


def test_solve_part_one_function_gets_corrent_argument():
    with pytest.raises(TypeError):
        solve_part_one()


def test_solve_part_one_function_returns_a_string():
    result = solve_part_one(
        ["move 2 from 4 to 9", "move 5 from 2 to 9", "move 1 from 5 to 1"]
    )
    assert isinstance(result, str)


def test_solve_part_two_function_gets_corrent_argument():
    with pytest.raises(TypeError):
        solve_part_two()


def test_solve_part_two_function_returns_a_string():
    result = solve_part_two(
        ["move 2 from 4 to 9", "move 5 from 2 to 9", "move 1 from 5 to 1"]
    )
    assert isinstance(result, str)
