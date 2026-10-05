def create_dict(name: str, age: int) -> dict[str, int]:
    return {name: age}

def list_to_dict(words: list[str]) -> dict[str, int]:
    return {word: indx for indx, word in enumerate(words)}



# don't modify code below this line
print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))
