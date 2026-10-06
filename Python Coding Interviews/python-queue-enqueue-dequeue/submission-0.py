from typing import Deque
from collections import deque


def rotate_list(arr: list[int], k: int) -> Deque[int]:
    queue = deque(arr)

    for _ in range(k):
        elem = queue.popleft()
        queue.append(elem)

    return queue

# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
