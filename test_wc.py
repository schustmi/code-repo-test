from wc import word_count


def test_word_count_basic():
    assert word_count("hello world") == 2


def test_word_count_single_word():
    assert word_count("hello") == 1


def test_word_count_empty_string():
    assert word_count("") == 0


def test_word_count_whitespace_only():
    assert word_count("   ") == 0


def test_word_count_irregular_whitespace():
    assert word_count("hello   world\tfoo\nbar") == 4


def test_word_count_leading_trailing_whitespace():
    assert word_count("  hello world  ") == 2
