class Solution:
    def maxArea(self, heights: list[int]) -> int:
        """Brute Force    TLE

        T = O(n^2), S = O(1)
        """
        # max_water = 0
        # for i in range(len(heights) - 1):
        #     for j in range(i + 1, len(heights)):
        #         max_water = max(max_water, (j - i) * min(heights[i], heights[j]))

        # return max_water


        """Two Pointers

        T = O(n), S = O(n)
        """
        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:
            max_water = max(max_water, (right - left) * min(heights[left], heights[right]))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_water
