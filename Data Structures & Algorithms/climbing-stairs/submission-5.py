import math


class Solution:
    def climbStairs(self, n: int) -> int:
        """Brute Force    TLE

        T = O(2^n), S = O(n)
        """
        # def dfs(step: int) -> int:
        #     if step >= n:
        #         return step == n
        #     return dfs(step + 1) + dfs(step + 2)

        # return dfs(0)


        """DP Top Down - Memoization

        T = O(n), S = O(n)
        """
        # cache = [-1] * n
        # def dfs(step: int) -> int:
        #     if step >= n:
        #         return step == n

        #     if cache[step] != -1:
        #         return cache[step]

        #     cache[step] = dfs(step + 1) + dfs(step + 2)
        #     return cache[step]

        # return dfs(0)


        """DP Bottom Up - Tabulation

        T = O(n), S = O(n)
        """
        # if n <= 2:
        #     return n

        # dp = [0] * (n + 1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]


        """DP Space Optimized

        T = O(n), S = O(1)
        """
        # if n <= 2:
        #     return n

        # dp1 = 1
        # dp2 = 2
        # for i in range(3, n + 1):
        #     temp = dp2
        #     dp2 += dp1
        #     dp1 = temp

        # return dp2


        """Math

        T = O(log n), S = O(1)
        """
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        n += 1
        return round((phi**n - psi**n) / sqrt5)
