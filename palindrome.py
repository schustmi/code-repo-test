def is_palindrome(text: str) -> bool:
    """Return True if text is a palindrome, ignoring case and spaces."""
    normalized = text.replace(" ", "").lower()
    return normalized == normalized[::-1]
