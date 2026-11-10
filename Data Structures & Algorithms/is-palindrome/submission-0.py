class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Reverse String

        T = O(3n) = O(n), S = O(2n) = O(n)
        """
        normalized_str = ''.join(char.lower() for char in s if char.isalnum())
        return normalized_str == normalized_str[::-1]
