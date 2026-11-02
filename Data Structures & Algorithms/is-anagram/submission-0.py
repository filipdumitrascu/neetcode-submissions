class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Sorting

        n - len(s), m - len(t)
        T = O(n log n + m log m), S = O(n + m)
        """
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
