import heapq


class KthLargest:
    """Brute Force (list and sort)
    
    Ne dorim al k lea cel mai mare element ditr-un stream de valori
    Approachul straight forward este sa inseram noua valoare, sa sortam
    lista de fiecare data si sa alegem elementul de pe pozitia 
    'len(arr) - k'. Sortarea este bottleneck, se intampla la fiecare
    call de add().

    m - num of calls add(), n - current size array
    T = O(m * n log n), S = O(n)
    """
    # def __init__(self, k: int, nums: list[int]):
    #     self.k = k
    #     self.arr = nums

    # def add(self, val: int) -> int:
    #     self.arr.append(val)
    #     self.arr.sort()

    #     return self.arr[len(self.arr) - self.k]



    """Min Heap

    Pentru a păstra al k-lea element ca mărime dintr-un stream de numere, nu este
    necesar să stocăm toate valorile. În schimb, trebuie doar să ținem evidența
    celor k elemente cu cea mai mare valoare întâlnita până în acel moment.

    Un min-heap de dimensiune k este perfect pentru acest scop:
    - Un min-heap păstrează întotdeauna cea mai mică valoare în vârf.
    - Dacă heap-ul conține cele k elemente cu cea mai mare valoare,
    atunci cel mai mic dintre ele este exact al k-lea ca mărime în ansamblu.

    De fiecare dată când apare un număr nou:
    - Dacă îl adăugăm și grămada depășește k, eliminăm elementul cel mai mic 
    deoarece acesta nu mai face parte din primele k cele mai mari.

    În acest fel, grămada păstrează întotdeauna exact primele k elemente, iar
    returnarea celui de-al k-lea cel mai mare se face în timp O(1).

    __init__: T = O(n log n), S = O(n)
    m adds:    T = O(m log k), S = O(k)
    """
    def __init__(self, k: int, nums: list[int]):
        self.min_heap = nums
        self.k = k

        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]
