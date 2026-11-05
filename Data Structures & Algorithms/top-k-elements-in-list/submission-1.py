import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """Sorting

        T = O(n log n), S = O(n)
        """
        num_to_freq = {}
        for num in nums:
            num_to_freq[num] = num_to_freq.get(num, 0) + 1

        freq_and_num = []
        for num, freq in num_to_freq.items():
            freq_and_num.append((freq, num))
        freq_and_num.sort(key=lambda pair: pair[0], reverse=True)

        return [pair[1] for pair in freq_and_num[:k]]
     
