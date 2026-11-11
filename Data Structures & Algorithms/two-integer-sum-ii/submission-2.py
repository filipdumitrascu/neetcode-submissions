class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """Brute Force    TLE

        T = O(n^2), S = O(1)
        """
        # for i in range(len(numbers) - 1):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]
        # return []


        """n Binary Searches

        T = O(n log n), S = O(1)
        """
        for i in range(len(numbers)):
            left = i + 1
            right = len(numbers) - 1
            complement = target - numbers[i]

            while left <= right:
                mid = left + (right - left) // 2

                if numbers[mid] == complement:
                    return [i + 1, mid + 1]
                elif numbers[mid] < complement:
                    left = mid + 1
                else:
                    right = mid - 1
        return []
