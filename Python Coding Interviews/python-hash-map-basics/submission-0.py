def build_hash_map(keys: list[str], values: list[int]) -> dict[str, int]:
    res = {}
    for key, value in zip(keys, values):
        res[key] = value
    return res

def get_values(hash_map: dict[str, int], keys: list[str]) -> list[int]:
    res = []
    for key in keys:
        res.append(hash_map[key])
    return res


# do not modify below this line
print(build_hash_map(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(build_hash_map(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(build_hash_map(["Doug", "Bob", "Tommy"], [80, 90, 100]))

print(get_values({"Alice": 90, "Bob": 80, "Charlie": 70}, ["Alice", "Bob", "Charlie"]))
print(get_values({"Jane": 25, "Charlie": 60, "Carol": 100, }, ["Jane", "Carol"]))
print(get_values({"X": 205, "Y": 78, "Z": 100}, ["Y"]))
