"""A tiny module for the briar demos."""


def greet(name):
    return f"Hello, {name}!"


def shout(name=None):
    return greet(name).upper()
