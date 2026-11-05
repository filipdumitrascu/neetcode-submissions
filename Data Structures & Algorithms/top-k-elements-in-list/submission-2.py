import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """Sorting

        T = O(n log n), S = O(n)
        """
        # num_to_freq = {}
        # for num in nums:
        #     num_to_freq[num] = num_to_freq.get(num, 0) + 1

        # freq_and_num = []
        # for num, freq in num_to_freq.items():
        #     freq_and_num.append((freq, num))
        # freq_and_num.sort(key=lambda pair: pair[0], reverse=True)

        # return [pair[1] for pair in freq_and_num[:k]]


        """Min Heap

        T = O(n log k), S = O(n)
        """
        # num_to_freq = {}
        # for num in nums:
        #     num_to_freq[num] = num_to_freq.get(num, 0) + 1

        # min_heap = []
        # for num, freq in num_to_freq.items():
        #     heapq.heappush(min_heap, (freq, num))

        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)
        
        # return [pair[1] for pair in min_heap]        


        """Bucket Sort

        T = O(n), S = O(n)
        """
        num_to_freq = {}
        for num in nums:
            num_to_freq[num] = num_to_freq.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in num_to_freq.items():
            buckets[freq].append(num)

        result = []
        for i in range(len(nums), -1, -1):
            for elem in buckets[i]:
                result.append(elem)
                if len(result) == k:
                    return result

        return result
