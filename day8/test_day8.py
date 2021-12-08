import pytest


from day8 import day8


def test_parse_line():
    line = 'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe'
    expected = ['be', 'abcdefg', 'bcdefg', 'acdefg', 'bceg', 'cdefg', 'abdefg', 'bcdef', 'abcdf', 'bde'], \
        ['abcdefg', 'bcdef', 'bcdefg', 'bceg']
    assert day8.parse_line(line) == expected


def test_decode_by_lookup():
    assert day8.decode_by_lookup('ab', {'ab': 'cf'})  == 'cf'


@pytest.mark.parametrize('input, output', [
    ('cf', 'cf'),
    ('be', 'cf'),
    ('cbg', 'acf'),
    ('gcbe', 'bcdf'),
    ('dgebacf', 'abcdefg')
])
def test_decode_by_letter_count(input, output):
    assert day8.decode_by_letter_count(input) == output


def test_infer():
    decoder = {
        'be': 'cf',
        'b': 'f'
    }
    day8.infer(decoder)
    assert 'e' in decoder
