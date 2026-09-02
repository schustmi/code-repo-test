import pytest

from palindrome import is_palindrome


@pytest.mark.parametrize(
    "text, expected",
    [
        ("racecar", True),
        ("RaceCar", True),
        ("nurses run", True),
        ("A man a plan a canal Panama", True),
        ("hello", False),
        ("", True),
        ("a", True),
    ],
)
def test_is_palindrome(text, expected):
    assert is_palindrome(text) is expected
