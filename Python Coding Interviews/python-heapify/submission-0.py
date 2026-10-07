import heapq


def heapify_strings(strings: list[str]) -> list[str]:
    heapq.heapify(strings)
    return strings

def heapify_integers(integers: list[int]) -> list[int]:
    heapq.heapify(integers)
    return integers

def heap_sort(nums: list[int]) -> list[int]:
    heapq.heapify(nums)
    result = []
    
    while nums:
        result.append(heapq.heappop(nums))
    return result


# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))
