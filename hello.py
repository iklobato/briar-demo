"""A tiny module for the briar demos."""


def greet(name):
    return f"Hello, {name}!"


def whisper(name=None):
    return greet(name).lower()
