import heapq

def heap_pop(heap: list[int]) -> list[int]:
    result = []
    while len(heap) > 0:
        result.append(heapq.heappop(heap))
    return result

# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
