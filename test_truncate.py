import pytest

from truncate import truncate


def test_no_truncation_when_shorter():
    assert truncate("hello", 10) == "hello"


def test_no_truncation_when_equal():
    assert truncate("hello", 5) == "hello"


def test_truncates_and_appends_ellipsis():
    result = truncate("hello world", 8)
    assert result == "hello..."
    assert len(result) == 8
    assert result.startswith("hello")


@pytest.mark.parametrize(
    "text,max_length",
    [
        ("hello world", 8),
        ("a" * 100, 10),
        ("short", 3),
        ("", 0),
        ("abcdef", 6),
        ("abcdef", 0),
    ],
)
def test_truncate_result_length_never_exceeds_max_length(text, max_length):
    assert len(truncate(text, max_length)) <= max_length


@pytest.mark.parametrize("max_length", [0, 1, 2, 3])
def test_small_max_length_edge_case(max_length):
    result = truncate("hello world", max_length)
    assert len(result) <= max_length
    assert result == "..."[:max_length]


def test_empty_string():
    assert truncate("", 10) == ""


def test_negative_max_length_raises():
    with pytest.raises(ValueError):
        truncate("hello", -1)
