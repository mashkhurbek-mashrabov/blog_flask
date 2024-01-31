import pytest

from add import add


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (1, 1, 2),
    (1, 0, 1),
    (0, 0, 0)
])
def test_add(a, b, expected):
    got = add(a, b)
    assert got == expected, f"{expected=}, {got=}"
