import pytest

from day4 import day4

def test_mark_grid():
    grid = [[1, 2], [3, 4]]
    assert day4.mark_grid(grid, 1) == [['*', 2], [3, 4]]


def test_grid_wins_diagonal_false():
    grid = [['*', 2], [3, '*']]
    assert day4.grid_wins(grid) == False


def test_grid_wins_horizontal_true():
    grid = [['*', '*'], [3, 4]]
    assert day4.grid_wins(grid) == True


def test_grid_wins_vertical_true():
    grid = [['*', 2], ['*', 4]]
    assert day4.grid_wins(grid) == True


