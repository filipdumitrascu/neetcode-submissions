class Solution:
    def rob(self, nums: list[int]) -> int:
        """Brute Force    TLE

        T = O(2^n), S = O(n)
        """
        # def dfs(i: int) -> int:
        #     if i >= len(nums):
        #         return 0
        #     return max(dfs(i + 1), nums[i] + dfs(i + 2))
        # return dfs(0)


        """DP Top Down Memoization

        T = O(n), S = O(n)
        """
        # memo = [-1] * len(nums)
        # def dfs(i: int) -> int:
        #     if i >= len(nums):
        #         return 0

        #     if memo[i] != -1:
        #         return memo[i]

        #     memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
        #     return memo[i]
        # return dfs(0)


        """DP Bottom Up Tabulation

        T = O(n), S = O(n)
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[len(nums) - 1]
