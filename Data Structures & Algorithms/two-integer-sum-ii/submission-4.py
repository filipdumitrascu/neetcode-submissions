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
        # for i in range(len(numbers)):
        #     left = i + 1
        #     right = len(numbers) - 1
        #     complement = target - numbers[i]

        #     while left <= right:
        #         mid = left + (right - left) // 2

        #         if numbers[mid] == complement:
        #             return [i + 1, mid + 1]
        #         elif numbers[mid] < complement:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        # return []


        """Hash map

        T = O(n), S = O(n)
        """
        # seen = {}
        # for i in range(len(numbers)):
        #     complement = target - numbers[i]
        #     if complement in seen:
        #         return [seen[complement], i + 1]
        #     seen[numbers[i]] = i + 1
        # return []


        """Two pointers

        T = O(n), S = O(1)
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left + 1, right + 1]
            
            if current > target:
                right -= 1
            else:
                left += 1
        return []
