import heapq
import random


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """Sorting

        Dacă sortezi întregul tablou, toate elementele vor fi aranjate de la
        cel mai mic la cel mai mare.
        Odată sortat:
        - Cel mai mare element se află pe ultima poziție.
        - Al doilea cel mai mare se află cu o poziție înaintea acestuia.
        - Al k-lea cel mai mare se află pur și simplu la indexul n - k.

        Așadar, problema devine:
        → Sortează tabloul și alege elementul care se află la k pași de sfârșit.

        Aceasta este o abordare simplă, dar nu cea mai eficientă, deoarece
        sortarea durează O(n log n).

        T = O(n log n), S = O(n)
        """
        # nums.sort()
        # return nums[len(nums) - k]



        """Min Heap

        În loc să sortăm întregul tablou, trebuie doar să ținem evidența celor
        k elemente cele mai mari întâlnite până în acel moment.

        Un min-heap este perfect pentru acest scop:
        -Un min-heap păstrează întotdeauna elementul cel mai mic în vârf.
        -Dacă menținem un heap de dimensiunea k, atunci:
         heap-ul va conține întotdeauna cele k elemente cele mai mari întâlnite
          până în acel moment.
         rădăcina heap-ului (cel mai mic dintre acești k) va fi al k-lea element
          ca mărime.

        Proces:
        -Adăugăm elemente în heap.
        -Dacă heap-ul depășește mărimea k, eliminăm elementul cel mai mic.
        -La final, rădăcina heap-ului este exact al k-lea element ca mărime.

        Astfel se evită sortarea întregului tablou și se menține un consum
        redus de memorie.

        T = O(n log k), S = O(k)
        """
        # # return heapq.nlargest(k, nums)[-1]
        # min_heap = []

        # for num in nums:
        #     heapq.heappush(min_heap, num)

        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)

        # return min_heap[0]



        """Quick Select

        Quick Select este un algoritm de selecție care funcționează similar cu
        QuickSort, dar explorează doar partea din array care conține răspunsul.

        Ideea principală:
        -Alege un pivot.
        -Reorganizează elementele astfel încât:
         toate numerele mai mici sau egale cu pivotul să fie mutate în stânga,
         toate numerele mai mari să fie mutate în dreapta.
        -După partiționare, pivotul ajunge în poziția corectă, sortată.
        -În loc să sortăm întregul arrau, verificăm:
         Dacă poziția finală a pivotului este indexul dorit → răspunsul a fost
          găsit.
         În caz contrar, aplicăm recursivitatea doar în partea în care se află
          indexul țintă.

        Deoarece eliminăm jumătate din array de fiecare dată, această abordare
        este, în medie, mult mai rapidă decât sortarea completă.

        Pentru al k-lea cel mai mare:
        -Convertiți-l în indexul corespunzător în ordinea sortată:
         index = n - k

        Apoi utilizați Quick Select pentru a găsi valoarea care ar apărea
        la acel index.

        T = O(n), S = O(n)
        """
        def helper(nums: list[int], k: int):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)

            if k <= len(left):
                return helper(left, k)

            if len(left) + len(mid) < k:
                return helper(right, k - len(left) - len(mid))

            return pivot

        return helper(nums, k)
