import pytest

from day3 import day3

def test_transpose():
    assert day3.transpose(((1, 2), (3, 4))) == ((1, 3), (2, 4))


def test_least_common():
    assert day3.least_common((0, 0, 1, 0, 0)) == 1


def test_most_common():
    assert day3.most_common((0, 0, 1, 0, 0)) == 0


def test_most_common_default_1():
    assert day3.most_common((0, 1), 1) == 1


def test_least_common_default_0():
    assert day3.least_common((0, 1), 0) == 0


def test_gamma():
    numbers = ((0, 0, 1), (1, 1, 1), (1, 0, 0))
    transposed = day3.transpose(numbers)
    assert day3.gamma(transposed) == 5  # 101


def test_epsilon():
    numbers = ((0, 0, 1), (1, 1, 1), (1, 0, 0))
    transposed = day3.transpose(numbers)
    assert day3.epsilon(transposed) == 2  # 010

