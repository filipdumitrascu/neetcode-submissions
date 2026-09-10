class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Sorting

        If two strings are anagrams, they must contain exactly the same
        characters with the same frequencies. By sorting both strings, all
        characters will be arranged in a consistent order. If the two sorted
        strings are identical, then every character and its count match,
        which means the strings are anagrams.

        T  = O(n log n), S = O(n)
        """
        # if len(s) != len(t):
        #     return False
        
        # return sorted(s) == sorted(t)


        """Array (for ASCII characters)

        Instead of sorting, we can count how many times each character appears
        in both strings. Since the problem guarantees lowercase English letters,
        we can use a fixed-size array of length 26 to count character frequencies.
        As we iterate through both strings simultaneously, we increment the
        count for each character in s and decrement the count for each character
        in t. If the strings are anagrams, every increment will be matched by a
        corresponding decrement, and all values in the array will end at 0.
        This approach is efficient because it avoids sorting and uses constant space.

        T = O(n), S = O(26) = O(1)
        """
        # if len(s) != len(t):
        #     return False

        # char_freq: list[int] = [0] * 26
        # for i in range(len(s)):
        #     char_freq[ord(s[i]) - ord('a')] += 1
        #     char_freq[ord(t[i]) - ord('a')] -= 1
        
        # return all(freq == 0 for freq in char_freq)


        """Hash Map (for Unicode characters)

        The approach is similar to the previous one, except that the hash map can be used
        for Unicode characters, so we don't need to specify an exact, fixed number of
        characters that may be present in the strings.
        
        T = O(n), S = O(u) = O(1)
        """
        if len(s) != len(t):
            return False
        
        char_freq: dict[str, int] = {}
        for i in range(len(s)):
            char_freq[s[i]] = char_freq.get(s[i], 0) + 1
            char_freq[t[i]] = char_freq.get(t[i], 0) - 1

        return all(freq == 0 for freq in char_freq.values())
