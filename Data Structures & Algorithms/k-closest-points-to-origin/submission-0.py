import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """Sorting

        Pentru a găsi cele k puncte cele mai apropiate de originea (0, 0),
        comparăm punctele în funcție de distanța lor față de origine. Deoarece
        distanța reală implică o rădăcină pătrată, iar rădăcina pătrată
        păstrează ordinea, putem compara punctele folosind distanța la pătrat:

        d^2 = x^2 + y^2

        Astfel se evită calculele inutile, iar această metodă este suficientă
        pentru sortare.

        Dacă sortăm toate punctele în funcție de această distanță la pătrat,
        atunci primele k puncte din ordinea sortată trebuie să fie cele mai
        apropiate k puncte.

        T = O(n log n), S = O(n)
        """
        # points.sort(key=lambda point: point[0] ** 2 + point[1] ** 2)
        # return points[:k]



        """Min Heap

        Un min-heap afișează întotdeauna mai întâi elementul cel mai mic.
        Dacă introducem fiecare punct într-un min-heap, folosind ca prioritate
        distanța pătrată față de origine, atunci:

        -Punctul cel mai apropiat se va afla în vârf.
        -Următorul punct cel mai apropiat va fi eliminat apoi, și așa mai
        departe.
        Deci, dacă eliminăm de k ori din heap, obținem exact cele k puncte cele
        mai apropiate.

        Acest lucru funcționează deoarece heap-ul păstrează întotdeauna
        distanțele cele mai mici în față.

        T = O(n + k log n), S = O(n)
        """
        # min_heap = []

        # for x, y in points:
        #     dist = x ** 2 + y ** 2
        #     min_heap.append((dist, x, y))

        # heapq.heapify(min_heap)
        # res = []

        # while k > 0:
        #     dist, x, y = heapq.heappop(min_heap)
        #     res.append([x, y])
        #     k -= 1

        # return res



        """Quick Select

        Vrem cele k puncte cele mai apropiate, dar NU este necesar ca acestea
        să fie sortate.
        Acesta este un caz de utilizare perfect pentru QuickSelect, aceeași
        idee folosită în etapa de partiționare a algoritmului QuickSort:

        -Alege un punct pivot.
        -Partiționează toate punctele în:
          punctele mai apropiate decât punctul pivot
          punctele mai îndepărtate decât punctul pivot
        -După partiționare, punctul pivot ajunge la poziția corectă în ordinea
        finală sortată.
        -Dacă punctul pivot ajunge la indexul p:
          Dacă p == k, atunci partea stângă conține deja cele k puncte cele
          mai apropiate.
          Dacă p < k, căutăm în jumătatea dreaptă.
          Dacă p > k, căutăm în jumătatea stângă.

        Astfel se evită sortarea completă a tabloului și se execută în timp
        mediu O(n).

        T = O(n), S = O(1)
        """
        def squared_distance(point: list[int]) -> int:
            """Calculate and return the squared Euclidean distance."""
            return point[0] ** 2 + point[1] ** 2

        def choose_pivot(points: list[list[int]], left: int, right: int) -> list[int]:
            """Choose a pivot element of the list"""
            return points[left + (right - left) // 2]

        def partition(points: list[list[int]], left: int, right: int) -> int:
            """Partition the list around the pivot value"""
            pivot = choose_pivot(points, left, right)
            pivot_dist = squared_distance(pivot)
            while left < right:
                # Iterate through the range and swap elements to make sure
                # that all points closer than the pivot are to the left
                if squared_distance(points[left]) >= pivot_dist:
                    points[left], points[right] = points[right], points[left]
                    right -= 1
                else:
                    left += 1
            # Ensure the left pointer is just past the end of
            # the left range then return it as the new pivotIndex
            if squared_distance(points[left]) < pivot_dist:
                left += 1
            return left

        left, right = 0, len(points) - 1
        pivot_index = len(points)
        while pivot_index != k:
            # Repeatedly partition the list
            # while narrowing in on the kth element
            pivot_index = partition(points, left, right)
            if pivot_index < k:
                left = pivot_index
            else:
                right = pivot_index - 1
        # Return the first k elements of the partially sorted list
        return points[:k]
