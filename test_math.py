import pytest


def add_two_numbers(a, b):
    return a + b


#  the above method named => add_two_numbers, returns a+b

@pytest.mark.alltests
@pytest.mark.math
def test_small_numbers():
    assert add_two_numbers(20, 30) == 50, "The sum of a and b should be 50"


@pytest.mark.alltests
@pytest.mark.math
def test_large_numbers():
    assert add_two_numbers(200, 200) == 400, "The sum of a and b should be 400"
