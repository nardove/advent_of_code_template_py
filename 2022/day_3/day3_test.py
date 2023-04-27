from day3 import *
import pytest


def test_parse_returns_a_list():
    parsed = parse("./input.txt")
    assert isinstance(parsed, list)


def test_solve_part_one_gets_an_argument():
    with pytest.raises(TypeError):
        solve_part_one()


def test_solve_part_one_returns_a_number():
    result = solve_part_one(["foo", "barr"])
    assert isinstance(result, int)


def test_solve_part_two_gets_an_argument():
    with pytest.raises(TypeError):
        solve_part_two([])


def test_solve_part_two_returns_a_number():
    result = solve_part_two(["foo", "bar", "baz"])
    assert isinstance(result, int)
