import collections


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """Sorting

        n - num of strings, m - max len
        T = O(n * m log m), S = O(n * m)
        """
        groups = collections.defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            groups[sorted_s].append(s)

        return list(groups.values())
