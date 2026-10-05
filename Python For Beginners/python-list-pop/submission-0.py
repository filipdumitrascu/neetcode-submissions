def remove_from_list(my_list: list[int], index: int) -> list[int]:
    my_list.pop(index)
    return my_list

def pop_n_from_list(my_list: list[int], n: int) -> list[int]:
    for _ in range(n):
        my_list.pop()
    return my_list


# don't modify below this line
print(remove_from_list([1, 2, 3, 4, 5], 2))
print(remove_from_list([1, 2, 3, 4, 5], 0))
print(remove_from_list([1, 2, 3, 4, 5], 4))

print(pop_n_from_list([1, 2, 3, 4, 5], 2))
print(pop_n_from_list([1, 2, 3, 4, 5], 0))
print(pop_n_from_list([1, 2, 3, 4, 5], 5))
