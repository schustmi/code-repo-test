from shout import shout


def test_shout():
    assert shout("hello") == "HELLO!"


def test_shout_mixed_case():
    assert shout("Already Loud") == "ALREADY LOUD!"
