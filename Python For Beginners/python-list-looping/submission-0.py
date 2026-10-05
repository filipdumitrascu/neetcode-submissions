import functools

def count_x(nums: list[int], x: int) -> int:
    return functools.reduce(
        lambda result, cur: result + 1 if cur == x else result,
        nums,
        0
    )



# do not modify below this line
print(count_x([1, 2, 5, 6, 5], 5))
print(count_x([4, 3, 6, 1, 6], 5))
print(count_x([4, 7, 7, 6, 7, 6], 7))
