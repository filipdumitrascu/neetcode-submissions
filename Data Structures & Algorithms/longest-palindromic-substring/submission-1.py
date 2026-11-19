class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Brute Force    TLE

        T = O(n^3), S = O(n)
        """
        # res, res_len = "", 0

        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         left, right = i, j
        #         while left < right and s[left] == s[right]:
        #             left += 1
        #             right -= 1

        #         if left >= right and res_len < (j - i + 1):
        #             res = s[i : j + 1]
        #             res_len = j - i + 1
        # return res


        """DP

        T = O(n^2), S = O(n^2)
        """
        res_idx, res_len = 0, 0
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if res_len < (j - i + 1):
                        res_idx = i
                        res_len = j - i + 1

        return s[res_idx: res_idx + res_len]
