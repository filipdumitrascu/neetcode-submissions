def get_dict_keys(age_dict: dict[str, int]) -> list[str]:
    return [name for name in age_dict.keys()]

def get_dict_values(age_dict: dict[str, int]) -> list[int]:
    return [age for age in age_dict.values()]

# do not modify below this line
dict_1 = {"John": 25, "Doe": 30, "Jane": 22}
dict_2 = {"NeetCode": 24, "NeetCode2": 25, "NeetCode3": 26}

print(get_dict_keys(dict_1))
print(get_dict_keys(dict_2))

print(get_dict_values(dict_1))
print(get_dict_values(dict_2))
