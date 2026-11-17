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
        memo = [-1] * len(nums)
        def dfs(i: int) -> int:
            if i >= len(nums):
                return 0

            if memo[i] != -1:
                return memo[i]

            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return memo[i]
        return dfs(0)
