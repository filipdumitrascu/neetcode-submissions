class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Sorting

        n - len(s), m - len(t)
        T = O(n log n + m log m), S = O(n + m)
        """
        # if len(s) != len(t):
            # return False

        # return sorted(s) == sorted(t)


        """Frequency array (for ascii only)

        T = O(n + m), S = O(n + m)
        """
        if len(s) != len(t):
            return False

        char_freq = [0] * 26
        for i in range(len(s)):
            char_freq[ord(s[i]) - ord('a')] += 1
            char_freq[ord(t[i]) - ord('a')] -= 1

        return all(freq == 0 for freq in char_freq)
