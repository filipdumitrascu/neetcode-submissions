class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        """Brute Force    TLE

        T = O(n^2), S = O(1)
        """
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False


        """Sorting

        T = O(n log n), S = O(n)
        """
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False


        """Set (or hash map, one data
        structure with O(1) lookup)

        T = O(n), S = O(n)
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# # Test
# nums = [1, 2, 3, 3]
# sol = Solution()
# print(sol.hasDuplicate(nums))
