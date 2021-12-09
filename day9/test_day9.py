import pytest


from day9 import day9


heightmap = day9.read_file('day9/input_sample')


@pytest.mark.parametrize('origin_coordinates,adjacent_coordinates', [
    ((0, 0), [(1, 0), (0, 1), (1, 1)]),                  # top left corner
    ((9, 4), [(8, 3), (9, 3), (8, 4)]),                  # bottom right corner
    ((2, 0), [(1, 0), (3, 0), (1, 1), (2, 1), (3, 1)]),  # top edge
    ((9, 1), [(8, 0), (9, 0), (8, 1), (8, 2), (9, 2)]),  # right edge
    ((2, 2), [                                           # middle
        (1, 1), (2, 1), (3, 1),
        (1, 2), (3, 2),
        (1, 3), (2, 3), (3, 3)
    ])
])
def test_adjacent(origin_coordinates, adjacent_coordinates):
    assert day9.adjacent(origin_coordinates, heightmap) == adjacent_coordinates


@pytest.mark.parametrize('origin_coordinates,expected_result', [
    ((0, 0), False),
    ((1, 0), True),
    ((9, 0), True),
    ((2, 2), True),
    ((9, 1), False),
    ((6, 4), True),
    ((9, 4), False),
])
def test_low_point(origin_coordinates, expected_result):
    assert day9.low_point(origin_coordinates, heightmap) == expected_result