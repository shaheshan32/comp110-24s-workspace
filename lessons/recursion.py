"""Recursion practice."""

__author__ = "730396719"


def f(n: int, k: int) -> int:
    """Function for recursion."""
    if n == 0:
        return 0
    else:
        return n * k