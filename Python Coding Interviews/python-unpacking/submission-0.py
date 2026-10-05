def sum_3_integers(triplet: list[int]) -> int:
    elem1, elem2, elem3 = triplet
    return elem1 + elem2 + elem3

def compute_volume(box_dimensions: tuple[int, int, int]) -> int:
    width, height, depth = box_dimensions
    return width * height * depth


# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
