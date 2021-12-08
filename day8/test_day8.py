import pytest


from day8 import day8


def test_parse_line():
    line = 'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe'
    expected = ['be', 'abcdefg', 'bcdefg', 'acdefg', 'bceg', 'cdefg', 'abdefg', 'bcdef', 'abcdf', 'bde'], \
        ['abcdefg', 'bcdef', 'bcdefg', 'bceg']
    assert day8.parse_line(line) == expected


@pytest.mark.parametrize('input, output', [
    ('cf', 1),
    ('be', 1),
    ('acf', 7),
    ('cbg', 7),
    ('bcdf', 4),
    ('gcbe', 4),
    ('abcdefg', 8),
    ('dgebacf', 8)
])
def test_decode(input, output):
    assert day8.decode(input) == output
