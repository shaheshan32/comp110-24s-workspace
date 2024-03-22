"""Splitting a dictionary into two lists."""

__author__ = "730396719" 


def get_keys(test: dict[str, int]) -> list[str]:
    """Returns keys."""
    keys_list: list[str] = []
    for key in test:
        keys_list.append(key)
    return keys_list


def get_values(test: dict[str, int]) -> list[int]:
    """Returns values."""
    values_list: list[int] = []
    for values in test:
        values_list.append(test[values])
    return values_list