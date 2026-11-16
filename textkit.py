"""Small text helpers."""


def shout(text):
    """The text in capitals."""
    return text.upper()


def whisper(text):
    """The text in lower case."""
    return text.lower()


def count_words(text):
    """The number of words separated by whitespace."""
    return len(text.split())
