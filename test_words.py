from words import reverse_words


def test_reverse_words_multiple():
    assert reverse_words("hello world foo") == "foo world hello"


def test_reverse_words_single_word():
    assert reverse_words("hello") == "hello"


def test_reverse_words_empty_string():
    assert reverse_words("") == ""


def test_reverse_words_extra_whitespace():
    assert reverse_words("  hello   world  ") == "world hello"
