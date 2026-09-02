def reverse_words(text: str) -> str:
    """Reverse the order of words in the text."""
    return " ".join(text.split()[::-1])
