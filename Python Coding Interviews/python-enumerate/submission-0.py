def get_index_of_seven(nums: list[int]) -> int:
    for idx, elem in enumerate(nums):
        if elem == 7:
            return idx
    return -1    


def get_dist_between_sevens(nums: list[int]) -> int:
    first_idx = -1
    for idx, elem in enumerate(nums):
        if elem == 7 and first_idx != -1:
            return idx - first_idx
        if elem == 7:
            first_idx = idx
    return -1

# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
