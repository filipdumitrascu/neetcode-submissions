import heapq


def get_reverse_sorted(nums: list[int]) -> list[int]:
    heap = [-num for num in nums]
    heapq.heapify(heap)
    result = []

    while heap:
        result.append(-heapq.heappop(heap))
    return result


# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
