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
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.arr = nums

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()

        return self.arr[len(self.arr) - self.k]
