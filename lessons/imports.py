"""The file where I import stuff."""

from lessons import my_functions
from lessons.my_functions import my_variable

# or u can combine the above
from lessons.my_functions import add, my_variable

# __name__ = "__main__"
print(add(4,5))

#print(my_function.my_variable)
print(my_variable)