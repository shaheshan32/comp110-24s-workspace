""" Demonstrate Basic Syntax List"""

# Initalize an empty list 
grocery_list: list[str] = list()  # <- list constructor
grocery_list: list[str] = [] # <- called a literal list with nothing in it 

print(grocery_list)

# adding an item to a list
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")
print("After appending: ")
print(grocery_list)

# create an already populated list
grocery_list2: list[str] = ["bananas", "milk", "bread"]
print("Populated list")
print(grocery_list2)
grocery_list2.append("eggs")
print(grocery_list2)

#Indexing
print("Print first element string")
print(grocery_list[0])

# Modifying by index
print("Before change: ")
print(grocery_list)
grocery_list[1] = "almond milk"
print("After change: ")
print(grocery_list)

# You can have duplicates
grocery_list.append("almond milk")
print("Add almond milk again: ")
print(grocery_list)

# Length of a list
# Measing length
print("Length of list: ")
print(len(grocery_list))

# Removing an item 
grocery_list.pop(1)
print("After removing almond milk: ")
print(grocery_list)

# Function name: display
# Paramter: list[str]
# Return Nothing!
# Print out the list!
print("~*~ Functions! ~*~")



def display(word: list[str]) -> None:
    print(word)

display(grocery_list)
x = display(["Alyssa", "Erin", "AK"])
print(x)

# Create a list!
# Name: create
# Parameters: str and str
# Return list[str]
# Put both paramters into list 

def create(word1: str, word2: str) -> list[str]:
    my_list: list[str] = [word1, word2]
    return my_list

create("Hello", "World")
# this wont give any results 

print(create("Hello", "World"))

x: list[str] = create("Hello", "World")
print(x)



