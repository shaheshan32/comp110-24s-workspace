"""Ex04 Utils."""

__author__ = "730396719" 


def all(int: list[int], num: int) -> bool:
    """Do all the integers in the list match the number."""
    if len(int) == 0:
        return False
    
    idx = 0
    while idx < len(int):
        if int[idx] != num:
            return False
        idx += 1

    return True


def max(input: list[int]) -> int:
    """Find the max of the list given."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_int = input[0]
    idx = 1
    while idx < len(input):
        if input[idx] > max_int:
            max_int = input[idx]
        idx += 1
    
    return max_int


def is_equal(l1: list[int], l2: list[int]) -> bool:
    """Are both list of integers equal."""
    if len(l1) != len(l2):
        return False
    
    while len(l1):
        if l1.pop() != l2.pop():
            return False

    return True


def extend(l1: list[int], l2: list[int]) -> None:
    """Mutate list 1 onto list 2."""
    idx = 0
    while idx < len(l2):
        l1.append(l2[idx])
        idx += 1