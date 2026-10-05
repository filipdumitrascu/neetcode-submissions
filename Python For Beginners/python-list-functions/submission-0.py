def get_sum(nums: list[int]) -> int:
    # return sum(nums)
    res = 0
    for num in nums:
        res += num
    return res

def get_min(nums: list[int]) -> int:
    # return min(nums)
    res = float("inf")
    for num in nums:
        res = min(num, res)
    return res

def get_max(nums: list[int]) -> int:
    # return max(nums)
    res = float("-inf")
    for num in nums:
        res = max(num, res)
    return res

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
