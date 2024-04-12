"""Evaluates algorithms."""
__author__ = "730396719"

import matplotlib.pyplot as plt
from runtime_analysis_functions import evaluate_runtime, evaluate_memory_usage

START_SIZE: int = 0
END_SIZE: int = 1000

times_selection_sort = evaluate_runtime("selection_sort", START_SIZE, END_SIZE)
plt.plot(times_selection_sort)
plt.title("Runtime Analysis of Selection Sort - eshan")
plt.show()

times_insertion_sort = evaluate_runtime("insertion_sort", START_SIZE, END_SIZE)
plt.plot(times_insertion_sort)
plt.title("Runtime Analysis of Insertion Sort - eshan")
plt.show()

usage_selection_sort = evaluate_memory_usage("selection_sort", START_SIZE, END_SIZE)
plt.plot(usage_selection_sort)
plt.title("Memory Usage Analysis of Selection Sort - eshan")
plt.show()

usage_insertion_sort = evaluate_memory_usage("insertion_sort", START_SIZE, END_SIZE)
plt.plot(usage_insertion_sort)
plt.title("Memory Usage Analysis of Insertion Sort - eshan")
plt.show()