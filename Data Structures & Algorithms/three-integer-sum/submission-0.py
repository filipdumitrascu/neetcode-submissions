class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Brute Force    TLE

        Approachul straightforward pur si simplu incearca orice triplet posibil.
        Este garantat sa gasim toate tripleltele care insumate dau 0.
        Se foloseste un set pentru a elimina duplicatele iar prin sortare
        setul recunoaste triplete identice.

        m - num of triplets
        T = O(n^3), S = O(m)
        """
        # result = set()
        # nums.sort()

        # for i in range(len(nums) - 2):
        #     for j in range(i + 1, len(nums) - 1):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 result.add((nums[i], nums[j], nums[k]))

        # return [list(i) for i in result]



        """Two Pointers

        Dupa ce sortam arrayul, putem sa alegem un numar x si sa cautam celelate
        doua numere care adunate sa dea -x.
        Sortarea ajuta prin a scapa de duplicate usor si prin a aplica tehnica 
        de la Two Sum Input Array is sorted. (practic de n ori aceasta problema)

        T = O(n^2), S = O(1)
        """
        result = []
        nums.sort()

        for index, num in enumerate(nums):
            # exclude the same value from being used as first:
            if index > 0 and num == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums) - 1

            while left < right:
                target = num + nums[left] + nums[right]

                if target > 0:
                    right -= 1
                    continue

                if target < 0:
                    left += 1
                    continue

                result.append([num, nums[left], nums[right]])
                left += 1

                # skip the same solution
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

        return result
