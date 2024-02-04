"""Demonstrate the behavior of conditionals."""

user_input: str=input("Pick a number: ")
print(type(user_input))
user_number: int = int(user_input)
print(type(user_number))

# if user number is less than 10, print "small"
if user_number < 10:
    print("small")
else : # if user number >=10
    print("big")

# if user number is even, print :even"
if user_number % 2 == 0:
    print("even")
else : # user number is odd
    print("odd")

print(user_number)