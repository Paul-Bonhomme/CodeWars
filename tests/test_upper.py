from upper import is_uppercase
import pytest


@pytest.mark.parametrize("a, expected", [
    ("Pavel", False),
    ("PAVEL", True),
    ("Father", False),
    ("FATHER", True),
    ("Billy", True)
])
def test_func(a, expected):
    assert is_uppercase(a) == expected

