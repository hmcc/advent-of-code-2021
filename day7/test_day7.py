import pytest


from day7 import day7


def test_cost_one():
    assert day7.cost_one([16,1,2,0,4,2,7,1,2,14], 2) == 37



def test_cost_two():
    assert day7.cost_two([16,1,2,0,4,2,7,1,2,14], 5) == 168