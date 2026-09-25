import heapq


class MedianFinder:
    """Max and Min Heaps

    Pentru a găsi în mod eficient mediana pe măsură ce numerele continuă să
    sosească, împărțim fluxul în două jumătăți:

    -Un heap maxim (mic) care stochează jumătatea cu numerele mai mici.
        -Cel mai mare număr din această jumătate se află în vârf.
    -Un heap minim (mare) care stochează jumătatea cu numerele mai mari.
        -Cel mai mic număr din această jumătate se află în vârf.

    Obiectivul:
    -Să ne asigurăm că ambele grămezi au dimensiuni echilibrate
    (diferența de cel mult 1).
    -Să ne asigurăm că toate numerele din grămada mică sunt ≤ tuturor numerelor
    din grămada mare.

    Această configurație permite:
    -Mediana = vârful grămezii mai mari (dacă numărul de numere este impar)
    -Mediana = media celor două vârfuri (dacă numărul de numere este par)

    Astfel, se obține o complexitate de O(log n) pentru inserare și O(1) pentru
    căutarea medianei.

    addNum:      T = O(log n)
    findMedian:  T = O(1)
    """

    def __init__(self):
        self.small = []  # max heap
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        # balance heaps
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]

        if len(self.large) > len(self.small):
            return self.large[0]

        return (-self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
