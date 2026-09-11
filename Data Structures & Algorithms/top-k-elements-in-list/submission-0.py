import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """Sorting

        O solutie straight forward este sa calculam frecventa fiecarui numar,
        se sortam numerele dupa frecventa si sa le returnam pe cele mai 
        frecvente k.

        T = O(n log n), S = O(n)
        """
        # frequency: dict[int, int] = {}
        # for num in nums:
        #     frequency[num] = frequency.get(num, 0) + 1

        # freq_to_num: list[tuple[int, int]] = []
        # for num, freq in frequency.items():
        #     freq_to_num.append((freq, num))

        # freq_to_num.sort(key=lambda pair: pair[0], reverse=True)

        # return [pair[1] for pair in freq_to_num[:k]]



        """Min Heap

        Se poate eficientiza sortarea si extragerea celor mai frecvente k elemente
        folosind un min heap. Acesta poate pastra fix k elemente, introducerea si
        eliminearea facandu-se in log k iar mereu cand se depaseste size k, se
        elimina topul heapului, cea mai mica frecventa la acel moment. Astfel,
        la final in heap raman cele mai frecvente k elemente.

        T = O(n log k), S = O(n)
        """
        # frequency: dict[int, int] = {}
        # for num in nums:
        #     frequency[num] = frequency.get(num, 0) + 1

        # heap = []
        # for num, freq in frequency.items():
        #     heapq.heappush(heap, (freq, num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # return [elem[1] for elem in heap]



        """Bucket Sort

        Fiecare element din array apare de un anumit numar de ori, iar frecventa
        maxima posibila este lungimea arrayului. Putem folosi aceasta idee creand
        o lista in care indicele reprezinta o frecventa, iar la fiecare indice
        stocam toate numerele care apar exact de atatea ori.

        Dupa ce construim aceste grupuri, parcurgem lista de la cea mai mare
        frecventa posibila pana la cea mai mica si colectam numere din aceste
        grupuri pana cand avem k dintre ele. In acest fel, trecem direct la cele
        mai frecvente numere fara a sorta toate elementele in functie de frecventa,
        totul in timp liniar.

        T = O(n), S = O(n)
        """
        frequency: dict[int, int] = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        count = [[] for _ in range(len(nums) + 1)]

        for num, freq in frequency.items():
            count[freq].append(num)

        result = []
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
