import pytest


from day7 import day7


def test_fuel_cost():
    assert day7.fuel_cost([16,1,2,0,4,2,7,1,2,14], 2) == 37



