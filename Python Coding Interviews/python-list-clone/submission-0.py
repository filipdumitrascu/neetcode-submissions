def remove_element(arr: list[int], element: int) -> list[int]:
    copy = arr.copy()
    copy.remove(element)
    return copy


# do not modify below this line
arr = [1, 3, 5, 7, 9]

print(remove_element(arr, 3))
print(arr)
print(remove_element(arr, 9))
print(arr)
print(remove_element(arr, 1))
print(arr)
