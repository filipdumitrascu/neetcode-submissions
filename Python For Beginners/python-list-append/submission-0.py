def append_to_list(my_list: list[int], elements: list[int]) -> list[int]:
    for elem in elements:
        my_list.append(elem)

    return my_list
    # return my_list.extend(elements)


# do not modify below this line
print(append_to_list([1, 2, 3], [4, 5]))
print(append_to_list([], [1, 2, 3, 4]))
