def append_elements(arr1: list[int], arr2: list[int]) -> list[int]:
    for elem in arr2:
        arr1.append(elem)
    return arr1


def pop_n(arr: list[int], n: int) -> list[int]:
    if n > len(arr):
        return []
    
    for _ in range(n):
        arr.pop()
    return arr

def insert_at(arr: list[int], index: int, element: int) -> list[int]:
    arr.insert(index, element)
    return arr


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(pop_n([1, 2, 3, 4, 5], 2))
print(pop_n([1, 2, 3, 4, 5], 6))
print(pop_n([1, 2, 3, 4, 5], 5))

print(insert_at([1, 2, 3, 4, 5], 2, 6))
print(insert_at([1, 2, 3, 4], 6, 5))
