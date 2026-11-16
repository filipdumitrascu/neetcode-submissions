class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """Brute Force    TLE

        T = O(2^n), S = O(n)
        """
        # def dfs(step: int) -> int:
        #     if step >= len(cost):
        #         return 0
        #     return cost[step] + min(dfs(step + 1), dfs(step + 2))

        # return min(dfs(0), dfs(1))


        """Dp Top Down

        T = O(n), S = O(n)
        """
        # memo = [-1] * len(cost)
        # def dfs(step: int) -> int:
        #     if step >= len(cost):
        #         return 0

        #     if memo[step] != -1:
        #         return memo[step]
            
        #     memo[step] = cost[step] + min(dfs(step + 1), dfs(step + 2))
        #     return memo[step]

        # return min(dfs(0), dfs(1))


        """Dp Bottom Up
        
        T = O(n), S = O(n)
        """
        # n = len(cost)
        # dp = [0] * (n + 1)

        # for i in range(2, n + 1):
        #     dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        # return dp[n]


        """Dp Bottom Up, Space Optimized

        T = O(n), S = O(1)
        """
        dp1 = 0
        dp2 = 0
        for i in range(2, len(cost) + 1):
            temp = min(dp1 + cost[i - 1], dp2 + cost[i - 2])
            dp2 = dp1
            dp1 = temp
        return dp1