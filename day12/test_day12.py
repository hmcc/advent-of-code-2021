import pytest

from day12 import day12


path_map = day12.build_map('day12/input_sample')


@pytest.mark.parametrize('line, path', [
    ('start-A',['start', 'A']),
    ('HN-start',['HN', 'start']),
    ('kj-sa',['kj', 'sa']),
])
def test_parse(line, path):
    assert day12.parse(line) == path


@pytest.mark.parametrize('line, expected_result', [
    ('start', True),
    ('A', False),
    ('b', True),
    ('AA', False),
    ('cj', True)
])
def test_is_lowercase(line, expected_result):
    assert day12.is_lowercase(line) == expected_result



@pytest.mark.parametrize('path, next_step, expected_result', [
    (['start'], 'A', True),
    (['b', 'd'], 'b', False)
])
def test_can_step(path, next_step, expected_result):
    assert day12.can_step(path, next_step) == expected_result


@pytest.mark.parametrize('path, next_step, expected_result', [
    (['start'], 'A', True),
    (['b', 'd'], 'b', True),
    (['b', 'b', 'd'], 'b', False),
    (['a', 'a', 'b', 'd'], 'b', False)
])
def test_can_step_with_visit_twice(path, next_step, expected_result):
    assert day12.can_step(path, next_step, True) == expected_result
