"""Practice with dict and for loops"""

in_stock: dict[str, bool] = {"carrots": True, "beets": False, "apple": True}

for key in in_stock:
    #key is "carrots" "beets" "apples"
    # in_stock[key] is va;ies : True False True
    if in_stock[key]: # in_stocl[key] is True
        print(key)
