"""Mutating functions."""

__author__ = "730396719" 


def manual_append(word: list[int], num: int) -> None:
    """Adding to end."""
    word.append(num)


def double(word: list[int]) -> None:
    """Mulitply it by 2."""
    idx = 0
    while idx < len(word):
        word[idx] *= 2
        idx += 1



# WORKSPACE 
