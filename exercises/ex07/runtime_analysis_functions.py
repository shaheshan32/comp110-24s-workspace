"""Runtime analysis functions."""

import numpy as np
import timeit
import tracemalloc
from random import randint
# from sort_functions import selection_sort, insertion_sort

MAX_VAL: int = 10 ** 5
START_SIZE: int = 0
END_SIZE: int = 1000


def random_descending_list(n: int) -> list[int]:
    """Generate a list of random descending integers."""
    new_list: list[int] = []
    decreasing_list: list[int] = []
    for key in range(0, n - 1):
        decreasing_list.append(randint(START_SIZE, MAX_VAL))
    new_list.append(MAX_VAL)
    while len(decreasing_list) > 0:
        new_list.append(max(decreasing_list))
        decreasing_list.remove(max(decreasing_list))
    return new_list


def evaluate_runtime(fn_name, start_size: int, end_size: int) -> np.array:
    """Evaluate the runtime for different size inputs."""
    NUM_TRIALS: int = 1
    times: list[float] = []
    for inp_size in range(start_size, end_size + 1):
        l: list[int] = random_descending_list(inp_size)
        call_command: str = f"{fn_name}(l)"
        print(f"Trial {inp_size-start_size}/{end_size - start_size}")
        result = timeit.timeit(stmt=call_command, globals=locals(), number=NUM_TRIALS)
        times.append(result / NUM_TRIALS)
    print(f"Runtime of {fn_name} for input of size {end_size}: {round(result/NUM_TRIALS, 2)} seconds")
    return np.array(times)


def evaluate_memory_usage(fn_name, start_size: int, end_size: int):
    """Evaluates memory usage."""
    usage: list[float] = []
    for inp_size in range(start_size, end_size + 1):
        l: list[int] = random_descending_list(inp_size)
        print(f"Trial {inp_size-start_size}/{end_size - start_size}")
        tracemalloc.start()
        locals()[fn_name](l)
        result = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        usage.append(result[1])
    print(f"Memory usage of {fn_name} for input of size {end_size}: {result[1]} blocks of memory.")
    return np.array(usage)