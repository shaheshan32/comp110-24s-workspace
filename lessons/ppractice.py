"""Writing for loops."""

pets: list[str] = ["Louie", "Bo", "Bear"]

for elem in pets:
    print(f"Good boy, {elem}!")

def even_words(inp_list: list[str]) -> list[str]:
    """What it does is a mystery!"""
    even_list: list[str] = []
    for elem in inp_list:
        if len(elem) % 2 ==0:
            even_list.append(elem)
    return even_list

a: list[str] = ["Alyssa", "katie", "Anusha"]
even_words(a)

