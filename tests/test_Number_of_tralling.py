from Number_of_tralling import func_factor
import pytest

@pytest.mark.parametrize("n, expected", [
    (30, 7),
    (0, 0),
    (8, 1),
    (12, 2),
    (1000, 249)
])
def test_func(n, expected):
    assert func_factor(n) == expected

