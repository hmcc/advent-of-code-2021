import pytest

from collections import defaultdict
from day6 import day6

@pytest.mark.parametrize('input, output', [
    ({1: 1, 2: 1, 3: 2, 4: 1}, {0: 1, 1: 1, 2: 2, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}),
    ({0: 1, 1: 1, 2: 2, 3: 1}, {0: 1, 1: 2, 2: 1, 3: 0, 4: 0, 5: 0, 6: 1, 7: 0, 8: 1}),
    ({0: 1, 1: 2, 2: 1, 6: 1, 8: 1}, {0: 2, 1: 1, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 1, 8: 1}),
])
def test_age(input, output):
    assert day6.age(input) == output

@pytest.mark.parametrize('input, output', [
    ({1: 1, 2: 1, 3: 2, 4: 1}, 5),
    ({1: 5, 6: 5, 8: 4, 0: 3, 2: 3, 3: 2, 4: 2, 5: 1, 7: 1}, 26),
])
def test_count(input, output):
    assert day6.count(input) == output
