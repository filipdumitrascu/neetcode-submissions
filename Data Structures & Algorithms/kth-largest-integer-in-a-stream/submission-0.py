import heapq


class KthLargest:
    """Min Heap

    Pentru a păstra al k-lea element ca mărime dintr-un flux de numere, nu este
    necesar să stocăm toate valorile. În schimb, trebuie doar să ținem evidența
    celor k elemente cu cea mai mare valoare întâlnita până în acel moment.

    Un min-heap de dimensiune k este perfect pentru acest scop:
    -Un min-heap păstrează întotdeauna cea mai mică valoare în vârf.
    -Dacă heap-ul conține cele k elemente cu cea mai mare valoare,
    atunci cel mai mic dintre ele este exact al k-lea ca mărime în ansamblu.

    De fiecare dată când apare un număr nou:
    -Dacă îl adăugăm și grămada depășește k, eliminăm elementul cel mai mic 
    deoarece acesta nu mai poate face parte din primele k.

    În acest fel, grămada păstrează întotdeauna exact primele k elemente, iar
    recuperarea celui de-al k-lea cel mai mare se face în timp O(1).

    __init__: T = O(n log n), S = O(n)
    add:      T = O(log k), S = O(k)
    """

    def __init__(self, k: int, nums: list[int]):
        self.min_heap = nums
        self.k = k

        heapq.heapify(self.min_heap)

        while len(self.min_heap) > k:  # store the biggest k elements in increasing order
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]  # exactly the kth one


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
