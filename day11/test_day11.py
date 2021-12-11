import pytest

from day11 import day11


def from_array(values):
    return [[day11.DumboOctopus(value) for value in row] for row in values]


def to_array(octos):
    return [[octo.value for octo in row] for row in octos]


@pytest.mark.parametrize('input, output', [
    ([
        [1, 1, 1, 1, 1],
        [1, 9, 9, 9, 1],
        [1, 9, 1, 9, 1],
        [1, 9, 9, 9, 1],
        [1, 1, 1, 1, 1]
    ],[
        [3, 4, 5, 4, 3],
        [4, 0, 0, 0, 4],
        [5, 0, 0, 0, 5],
        [4, 0, 0, 0, 4],
        [3, 4, 5, 4, 3]
    ]
    ),
    ([
        [3, 4, 5, 4, 3],
        [4, 0, 0, 0, 4],
        [5, 0, 0, 0, 5],
        [4, 0, 0, 0, 4],
        [3, 4, 5, 4, 3]
    ],[
        [4, 5, 6, 5, 4],
        [5, 1, 1, 1, 5],
        [6, 1, 1, 1, 6],
        [5, 1, 1, 1, 5],
        [4, 5, 6, 5, 4]
    ]
    )
])
def test_process(input, output):
    octos = from_array(input)
    day11.process(octos)
    assert to_array(octos) == output


@pytest.mark.parametrize('iterations, expected_output', [
    (1, 0),
    (2, 35),
    (3, 80),
    (4, 96),
    (10, 204),
])
def test_part_one(iterations, expected_output):
    assert day11.part_one('day11/input_sample', iterations) == expected_output
