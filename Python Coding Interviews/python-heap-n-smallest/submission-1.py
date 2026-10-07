import heapq


def get_min_element(arr: list[int]) -> int:
    # return heapq.nsmallest(1, arr)[0]
    heap = []
    for elem in arr:
        heapq.heappush(heap, -elem)
        if len(heap) > 1:
            heapq.heappop(heap)    

    return -heap[0]

def get_min_4_elements(arr: list[int]) -> list[int]:
    # return heapq.nsmallest(4, arr)
    heap = []
    for elem in arr:
        heapq.heappush(heap, -elem)
        if len(heap) > 4:
            heapq.heappop(heap)

    return [-num for num in heap[::-1]]

def get_min_2_elements(arr: list[int]) -> list[int]:
    # result = heapq.nsmallest(2, arr)
    # return result[::-1]
    heap = []
    for elem in arr:
        heapq.heappush(heap, -elem)
        if len(heap) > 2:
            heapq.heappop(heap)

    return [-num for num in heap]



# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

