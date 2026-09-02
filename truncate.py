ELLIPSIS = "..."


def truncate(text: str, max_length: int) -> str:
    """Cut text to max_length characters, appending an ellipsis if cut."""
    if max_length < 0:
        raise ValueError("max_length must be non-negative")

    if len(text) <= max_length:
        return text

    if max_length <= len(ELLIPSIS):
        return ELLIPSIS[:max_length]

    return text[: max_length - len(ELLIPSIS)] + ELLIPSIS
