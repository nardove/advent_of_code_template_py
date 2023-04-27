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


def test_solve_part_one_function_returns_a_int_number():
    result = solve_part_one(["foo", "bar", "baz"])
    assert isinstance(result, int)


def test_solve_part_two_function_gets_corrent_argument():
    with pytest.raises(TypeError):
        solve_part_two()


def test_solve_part_two_function_returns_a_int_number():
    result = solve_part_two(["foo", "bar", "baz"])
    assert isinstance(result, int)
