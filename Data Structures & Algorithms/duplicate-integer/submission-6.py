class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        """Brute Force

        We can check every pair of different elements in the array and return
        true if any pair has equal values. This is the most intuitive approach
        because it directly compares all possible pairs, but it is also the
        least efficient since it examines every combination.

        T = O(n^2), S = O(1)
        """
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False


        """Sorting

        If we sort the array, then any duplicate values will appear
        next to each other. Sorting groups identical elements place together,
        so we can simply check adjacent positions to detect duplicates.
        This reduces the problem to a SINGLE linear scan after sorting, making
        it easy to identify if any value repeats.

        T = O(n log n), S = O(n)
        """
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i - 1] == nums[i]:
        #         return True
        # return False


        """Hash Set

        We can use a hash set to efficiently keep track of the values we have
        already encountered. As we iterate through the array, we check whether
        the current value is already present in the set. If it is, that means
        we've seen this value before, so a duplicate exists. Using a hash set
        allows constant-time lookups, making this approach much more efficient
        than comparing every pair.

        T = O(n), S = O(n)
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


        """Hash Set Length

        This approach uses the same idea as the previous hash set method: a set
        only stores unique values, so duplicates are automatically removed.
        Instead of checking each element manually, we simply compare the length of
        the set to the length of the original array. If duplicates exist, the set
        will contain fewer elements. The logic is identical to the earlier approach,
        this version is just a shorter and more concise implementation of it.

        T = O(n), S = O(n)
        """
        # return len(set(nums)) < len(nums)
