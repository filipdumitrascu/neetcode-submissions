class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Brute Force

        T = O(n^2), S = O(1)
        """
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []


        """Sorting

        T = O(n log n), S = O(n)
        """
        # nums_and_pos = []
        # for i, num in enumerate(nums):
        #     nums_and_pos.append((num, i))

        # nums_and_pos.sort()
        # left, right = 0, len(nums) - 1

        # while left < right:
        #     curr = nums_and_pos[left][0] + nums_and_pos[right][0]
        #     if curr == target:
        #         return [min(nums_and_pos[left][1], nums_and_pos[right][1]),
        #                 max(nums_and_pos[left][1], nums_and_pos[right][1])]

        #     if curr < target:
        #         left += 1
        #     else:
        #         right -= 1
        # return []


        """Hash map

        T = O(n), S = O(n)
        """
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_to_index:
                return [num_to_index[complement], i]

            num_to_index[num] = i
        return []
