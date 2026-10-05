def remove_keys(my_dict: dict[str, int], keys: list[str]) -> dict[str, int]:
    for key in keys:
        my_dict.pop(key, 0)
    return my_dict


# do not modify below this line
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"]))
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["d"]))
