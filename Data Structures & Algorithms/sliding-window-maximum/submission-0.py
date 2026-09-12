import heapq
import collections


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """Brute Force    TLE

        Pentru orice posibil window de size k, calculam maximul. Mutam windowul
        si de fiecare data calculam maximul. E un straighforward approach
        dar extrem de ineficient, nimic ingenios.

        T = O(n * k), S = O(1)
        """
        # result = []
        # for i in range(len(nums) - k + 1):
        #     max_i = nums[i]
        #     for j in range(i, i + k):
        #         max_i = max(max_i, nums[j])
        #     result.append(max_i)

        # return result



        """Heap

        Folosim un max heap in care punem tupluri (valoare, pozitie in array).
        Inseram elementele din dreapta pe masura ce mutam windowul si putem accesa
        mereu cel mai mare element din heap. Dar avand in vedere ca pe masura
        ce mutam windowul, elemente din stanga ies din acesta, e posibil ca topul
        heapului sa fie un element iesit. Ca urmare verificam poziita in array
        (pe care am inclus o in tuplu) si eliminam elemente din heap de la cel
        mai mare in jos pana dam de unul care este in window.

        T = O(n log n), S = O(n)
        """
        # heap = []  # max heap with (value, position)
        # result = []
        # for i in range(len(nums)):
        #     heapq.heappush(heap, (-nums[i], i))

        #     if i < k - 1:  # if no window has been created yet
        #         continue

        #     # In descending order the big elements that are not part
        #     # of the current window are removed from the max heap
        #     while heap[0][1] <= i - k:
        #         heapq.heappop(heap)

        #     result.append(-heap[0][0])
        # return result



        """Deque

        O coada (deque) ne ajuta sa urmarim in mod eficient valoarea maxima din
        interiorul ferestrei glisante. Ideea principala este ca coada sa stocheze
        indicii elementelor in ordine descrescatoare a valorilor acestora.
        Acest lucru garanteaza ca:

        Capatul din fata al cozii contine tntotdeauna indicele valorii maxime
        din fereastra curenta. Elementele mai mici aflate în spatele unuia mai
        mare sunt inutile (ele nu pot deveni niciodata valoarea maxima ulterior),
        asa ca le eliminam atunci cand introducem un numar nou.
        Dacă elementul din fata iese din fereastra, il eliminam.
        Prin mentinerea acestei structuri, fiecare element este adaugat si
        eliminat cel mult o singură data, oferind o solutie optima.

        T = O(n), S = O(n)
        """
        result = []
        queue = collections.deque()  # indexes

        left = 0
        for right in range(len(nums)):
            # Pop smaller previous values from queue
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)

            if left > queue[0]:  # remove the left value (window slided prev loop)
                queue.popleft()

            if right < k - 1:  # if no window has been created yet
                continue

            result.append(nums[queue[0]])
            left += 1  # slide the window

        return result
