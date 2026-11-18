"""A tiny module for the briar demos."""


def greet(name):
    return f"Hello, {name}!"


def farewell(name=None):
    if name is None:
        name = "world"
    return f"Goodbye, {name}!"
