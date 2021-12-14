import pytest

from day14 import day14


polymer, pairs = day14.parse_file('day14/input_sample')


def test_parse_file():
    polymer, pairs = day14.parse_file('day14/input_sample')
    assert polymer == 'NNCB'
    assert len(pairs) == 16
    assert pairs['CH'] == 'B'


@pytest.mark.parametrize('polymer, key, result', [
    ('NNCB', 'NN', [1]),
    ('NNCB', 'CH', []),
    ('NNCBNN', 'NN', [1, 5]),
])
def test_insertion_indices(polymer, key, result):
    assert day14.insertion_indices(polymer, key) == result


@pytest.mark.parametrize('polymer, insertions, result', [
    ('NNCB', {1: 'C'}, 'NCNCB'),
    ('NNCB', {}, 'NNCB'),
    ('NNCBNN', {1: 'C', 5: 'C'}, 'NCNCBNCN')
])
def test_insert(polymer, insertions, result):
    assert day14.insert(polymer, insertions) == result


@pytest.mark.parametrize('polymer, result', [
    ('NNCB', 'NCNBCHB'),
    ('NCNBCHB', 'NBCCNBBBCBHCB'),
    ('NBCCNBBBCBHCB', 'NBBBCNCCNBBNBNBBCHBHHBCHB'),
    ('NBBBCNCCNBBNBNBBCHBHHBCHB', 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'),
])
def test_process_once(polymer, result):
    pairs = {
       'CH': 'B',
       'HH': 'N',
       'CB': 'H',
       'NH': 'C',
       'HB': 'C',
       'HC': 'B',
       'HN': 'C',
       'NN': 'C',
       'BH': 'H',
       'NC': 'B',
       'NB': 'B',
       'BN': 'B',
       'BB': 'N',
       'BC': 'B',
       'CC': 'N',
       'CN': 'C' 
    }
    assert day14.process_once(polymer, pairs) == result


