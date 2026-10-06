def find_max_in_each_list(nested_arr: list[list[int]]) -> list[int]:
    result = []
    for arr in nested_arr:
        max_elem = float("-inf")
        for elem in arr:
            max_elem = max(max_elem, elem)

        result.append(max_elem)

    return result

# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
