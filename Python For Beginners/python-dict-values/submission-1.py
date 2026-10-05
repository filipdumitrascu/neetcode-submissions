def get_dict_values(age_dict: dict[str, int]) -> list[int]:
    # return [value for value in age_dict.values()]
    return list(age_dict.values())

# do not modify below this line
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35}))
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))
