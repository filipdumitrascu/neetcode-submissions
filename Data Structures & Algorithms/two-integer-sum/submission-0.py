class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Brute Force

        T = O(n^2), S = O(1)
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
