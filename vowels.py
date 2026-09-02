def count_vowels(text: str) -> int:
    """Return the number of vowels (a, e, i, o, u, case-insensitive) in text."""
    return sum(1 for char in text.lower() if char in "aeiou")
