import pytest

from day13 import day13


path_map = day13.parse_file('day12/input_sample')


@pytest.mark.parametrize('line, point', [
    ('6,10',(6, 10)),
    ('0,14',(0, 14)),
])
def test_parse_plot(line, point):
    assert day13.parse_plot(line) == point


@pytest.mark.parametrize('line, fold', [
    ('fold along y=7', ('y', 7)),
    ('fold along x=5', ('x', 5))
])
def test_parse_fold(line, fold):
    assert day13.parse_fold(line) == fold


def test_to_grid():
    plots = [
        (1, 3),
        (0, 5),
        (3, 4),
        (3, 0)
    ]
    grid = [
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
    ]
    assert day13.to_grid(plots) == grid


def test_fold_y():
    grid = [
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]
    ]
    assert day13.fold(grid, 'y', 2) == [
        [0, 0, 0, 1],
        [0, 1, 0, 0]
    ]


def test_fold_x():
    grid = [
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0]
    ]
    assert day13.fold(grid, 'x', 2) == [
        [0, 1],
        [1, 0],
        [0, 0],
        [0, 1],
    ]