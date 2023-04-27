from day2 import *
import pytest


def test_parse_input_returns_a_list():
    parse_input = parse("./input.txt")
    assert isinstance(parse_input, list)


def test_solve_gets_a_list_as_argument():
    with pytest.raises(TypeError):
        solve([])


def test_solve_returns_a_number():
    result = solve(["A X", "B Y", "C Z"])
    assert isinstance(result, int)
