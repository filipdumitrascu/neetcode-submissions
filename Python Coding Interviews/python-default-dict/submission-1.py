from collections import defaultdict
from typing import Dict


def count_chars(s: str) -> Dict[str, int]:
    res = defaultdict(int)

    for c in s:
        res[c] += 1
    return res

def nested_list_to_dict(nums: list[list[int]]) -> Dict[int, list[int]]:
    res = defaultdict(list)

    for sublist in nums:
        first = sublist[0]
        res[first].extend(sublist[1:])
    return res

# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
