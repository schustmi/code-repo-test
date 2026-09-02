from slug import slugify


def test_lowercases_text():
    assert slugify("HELLO") == "hello"


def test_replaces_single_non_alphanumeric_char():
    assert slugify("hello world") == "hello-world"


def test_collapses_runs_of_non_alphanumeric_chars():
    assert slugify("Hello   World!!!") == "hello-world"


def test_mixed_punctuation_and_whitespace():
    assert slugify("Hello, World -- Foo_Bar") == "hello-world-foo-bar"


def test_strips_leading_and_trailing_dashes():
    assert slugify("  Hello World!  ") == "hello-world"


def test_preserves_numbers():
    assert slugify("Room 42B") == "room-42b"


def test_empty_string():
    assert slugify("") == ""


def test_only_non_alphanumeric_characters():
    assert slugify("!!!") == ""
