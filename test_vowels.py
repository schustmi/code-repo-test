import pytest

from vowels import count_vowels


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello world", 3),
        ("aeiou", 5),
        ("AEIOU", 5),
        ("xyz", 0),
        ("", 0),
        ("Hello World", 3),
        ("Testing 1, 2, 3!", 2),
    ],
)
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected
