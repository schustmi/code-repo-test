import re


def slugify(text: str) -> str:
    """Lower-case text and collapse runs of non-alphanumeric chars into single dashes."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")
