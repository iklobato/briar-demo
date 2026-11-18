"""A tiny module for the briar demos."""


def greet(name):
    return f"Hello, {name}!"


def murmur(name):
    return greet(name).lower()
