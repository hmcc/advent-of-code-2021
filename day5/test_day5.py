import pytest

from day5 import day5

def test_read_input():
    coordinates = day5.read_input('day5/input_sample')
    assert coordinates == [
        ((0, 9), (5, 9)),
        ((8, 0), (0, 8)),
        ((9, 4), (3, 4)),
        ((2, 2), (2, 1)),
        ((7, 0), (7, 4)),
        ((6, 4), (2, 0)),
        ((0, 9), (2, 9)),
        ((3, 4), (1, 4)),
        ((0, 0), (8, 8)),
        ((5, 5), (8, 2))
    ]


def test_fill_x():
    filled = day5.fill_x((0, 9), (5, 9))
    assert filled == [(0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9)]


def test_fill_y():
    filled = day5.fill_y((2, 2), (2, 1))
    assert filled == [(2, 2), (2, 1)]


def test_fill_diagonal():
    filled = day5.fill_diagonal((6, 4), (2, 0))
    assert filled == [(6, 4), (5, 3), (4, 2), (3, 1), (2, 0)]


def test_fill_all_x_y():
    input = [
        ((0, 9), (5, 9)),
        ((8, 0), (0, 8)),
        ((9, 4), (3, 4))
    ]
    filled = day5.fill_all(input, day5.fill_x, day5.fill_y)
    assert filled == [
        (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9),
        (9, 4), (8, 4), (7, 4), (6, 4), (5, 4), (4, 4), (3, 4)
    ]


def test_fill_all_x_y_diagonal():
    input = [
        ((0, 9), (5, 9)),
        ((8, 0), (0, 8)),
        ((9, 4), (3, 4))
    ]
    filled = day5.fill_all(input, day5.fill_x, day5.fill_y, day5.fill_diagonal)
    assert filled == [
        (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9),
        (8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8),
        (9, 4), (8, 4), (7, 4), (6, 4), (5, 4), (4, 4), (3, 4)
    ]


def test_initialise_grid():
    coordinates = [
        (0, 2), (1, 0)
    ]
    assert day5.initialise_grid(coordinates) == [
        [0, 0],
        [0, 0],
        [0, 0]
    ]


def test_update_grid():
    initial_grid = [
        [0, 1],
        [1, 0]
    ]
    assert day5.update_grid(initial_grid, [(1, 0), (1, 1)]) == [
        [0, 2],
        [1, 1]
    ]