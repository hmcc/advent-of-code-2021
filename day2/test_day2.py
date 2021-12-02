import pytest

from day2 import day2

def test_parse_forward():
    assert day2.parse('forward 5') == ('forward', 5)


@pytest.mark.parametrize('direction, amount, expected_position, expected_depth', [
    ('forward', 5, 5, 0),
    ('down', 2, 0, 2),
    ('up', 1, 0, -1),
    ('what', 1, 0, 0),
])
def test_move_one(direction, amount, expected_position, expected_depth):
    location = day2.move_one(direction, amount, {
        'position': 0,
        'depth': 0
    })
    assert location['position'] == expected_position
    assert location['depth'] == expected_depth


@pytest.mark.parametrize('direction, amount, expected_position, expected_depth, expected_aim', [
    ('forward', 5, 5, 5, 1),
    ('down', 2, 0, 0, 3),
    ('up', 1, 0, 0, 0),
    ('what', 1, 0, 0, 1),
])
def test_move_two(direction, amount, expected_position, expected_depth, expected_aim):
    location = day2.move_two(direction, amount, {
        'position': 0,
        'depth': 0,
        'aim': 1
    })
    assert location['position'] == expected_position
    assert location['depth'] == expected_depth
    assert location['aim'] == expected_aim
