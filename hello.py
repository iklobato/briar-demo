"""A tiny module for the briar demos."""


def greet(name):
    return f"Hello, {name}!"


def hush(name):
    return greet(name).lower()[:-1]
