class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """Hash Set

        T = O(n), S = O(n)
        """
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num - 1 in nums_set:
                continue

            length = 0
            i = num
            while i in nums_set:
                i += 1
                length += 1
            longest = max(length, longest)

        return longest
