"""Functions that implement sorting algorithms."""

__author__ = "730396719"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm. Insert into an already sorted list."""
    sorted_idx = 0    
    while sorted_idx < len(x) - 1:
        unsorted_idx = sorted_idx + 1
        current_num = x[unsorted_idx] 
        while unsorted_idx > 0 and current_num < x[unsorted_idx - 1]:
            x[unsorted_idx] = x[unsorted_idx - 1]
            unsorted_idx -= 1
        x[unsorted_idx] = current_num
        sorted_idx += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    counter = 0
    while counter < len(x):
        min_idx = counter
        inside_counter = counter + 1
        while inside_counter < len(x):
            if x[inside_counter] < x[min_idx]:
                min_idx = inside_counter
            inside_counter += 1
        if min_idx != counter:
            swap = x[min_idx]
            x[min_idx] = x[counter]
            x[counter] = swap
        counter += 1
    return None