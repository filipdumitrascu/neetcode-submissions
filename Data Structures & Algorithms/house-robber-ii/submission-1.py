class Solution:
    def rob(self, nums: list[int]) -> int:
        """Brute Force    TLE

        T = O(2^n), S = O(n)
        """
        # if len(nums) == 1:
        #     return nums[0]

        # def dfs(i, flag):
        #     if i >= len(nums) or (flag and i == len(nums) - 1):
        #         return 0

        #     return max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag or i == 0))
        # return max(dfs(0, True), dfs(1, False))


        """Dp Top Down

        T = O(n), S = O(n)
        """
        if len(nums) == 1:
            return nums[0]

        memo = [[-1] * 2 for _ in range(len(nums))]

        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            if memo[i][flag] != -1:
                return memo[i][flag]
            memo[i][flag] = max(dfs(i + 1, flag),
                            nums[i] + dfs(i + 2, flag or (i == 0)))
            return memo[i][flag]

        return max(dfs(0, True), dfs(1, False))
