import pytest

from day14 import day14


polymer, pairs = day14.parse_file('day14/input_sample')


def test_parse_file():
    polymer, pairs = day14.parse_file('day14/input_sample')
    assert polymer == 'NNCB'
    assert len(pairs) == 16
    assert pairs['CH'] == 'B'


@pytest.mark.parametrize('polymer, result', [
    ({'NN': 1, 'NC': 1, 'CB': 1}, {'NC': 1, 'CN': 1, 'NB': 1, 'BC': 1, 'CH': 1, 'HB': 1}),
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


