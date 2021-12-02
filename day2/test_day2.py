from day2 import day2

def test_parse_forward():
    assert day2.parse('forward 5') == ('forward', 5)


def test_move_forward():
    assert (day2.move('forward', 5)) == (5, 0)


def test_move_down():
    assert (day2.move('down', 2)) == (0, 2)


def test_move_up():
    assert (day2.move('up', 1)) == (0, -1)


def test_move_unknown():
    assert (day2.move('what', 1)) == (0, 0)