class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """Brute Force    TLE

        T = O(n^2), S = O(1)
        """
        # res = [0] * len(nums)

        # for i in range(len(nums)):
        #     prod = 1

        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         prod *= nums[j]
            
        #     res[i] = prod
        # return res


        """Prefix and Suffix

        T = O(n), S = O(n)
        """
        # res = [0] * len(nums)
        # pref = [0] * len(nums)
        # suff = [0] * len(nums)

        # pref[0] = suff[len(nums) - 1] = 1
        # for i in range(1, len(nums)):
        #     pref[i] = nums[i - 1] * pref[i - 1]

        # for i in range(len(nums) - 2, -1, -1):
        #     suff[i] = nums[i + 1] * suff[i + 1]

        # for i in range(len(nums)):
        #     res[i] = pref[i] * suff[i]

        # return res


        """Prefix and Suffix optimal space

        T = O(n), S = O(1)
        """
        res = [0] * len(nums)

        pref = 1
        for i in range(len(nums)):
            res[i] = pref
            pref *= nums[i]

        suff = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suff
            suff *= nums[i]

        return res
