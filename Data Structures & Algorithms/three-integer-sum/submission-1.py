class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Brute Force    TLE

        T = O(n^3), S = O(m)
        """
        # res = set()
        # nums.sort()

        # for i in range(len(nums) - 2):
        #     for j in range(i + 1, len(nums) - 1):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 res.add((nums[i], nums[j], nums[k]))
        # return [list(i) for i in res]


        """Two Pointers

        T = O(n^2), S = O(n)
        """
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:  # skip duplicates
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                three_sum = a + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append((a, nums[left], nums[right]))
                    left += 1
                    right -= 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res
