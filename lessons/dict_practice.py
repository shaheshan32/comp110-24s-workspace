"""Practice with dictionaries."""

#empty one
#ice_cream: dict[str, int] = dict()

ice_cream: dict[str, int] = {'Chocolate': 12, 'Vanilla': 8, 'Strawberry': 5}
ice_cream["Mint"] = 3
print("After adding mint:")
print(ice_cream)

#Removing
ice_cream.pop("Mint")
print("After removing mint:")
print(ice_cream)


#Accessing
print(f"Number of vanilla numbers: {ice_cream['Vanilla']}")
print(ice_cream["Vanilla"])

#Update value
ice_cream["Vanilla"] += 1
print("After adding 1 vanilla")
print(ice_cream)
print(f"NUmber of vanilla orders: {ice_cream['Vanilla']}")

#Checking if in dictionary 
print("Mint" in ice_cream)
print("Chocolate" in ice_cream)


