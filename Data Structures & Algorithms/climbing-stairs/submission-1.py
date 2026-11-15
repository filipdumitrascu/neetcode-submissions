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
        cache = [-1] * n
        def dfs(step: int) -> int:
            if step >= n:
                return step == n

            if cache[step] != -1:
                return cache[step]

            cache[step] = dfs(step + 1) + dfs(step + 2)
            return cache[step]

        return dfs(0)
