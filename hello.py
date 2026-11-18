"""A tiny module for the briar demos."""


def greet(name):
    return f"Hello, {name}!"


def hush(name):
    """Return the greeting for name in lowercase, without the trailing punctuation."""
    return greet(name).lower()[:-1]
