class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Reverse String

        T = O(3n) = O(n), S = O(2n) = O(n)
        """
        # normalized_str = ''.join(char.lower() for char in s if char.isalnum())
        # return normalized_str == normalized_str[::-1]


        """Two pointers

        T = O(n), S = O(1)
        """
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
