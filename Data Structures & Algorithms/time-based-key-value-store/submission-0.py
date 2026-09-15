import collections


class TimeMap:
    """Binary Search on Timestammps

    Fiecare cheie stocheaza valorile sale in ordinea in care au fost inserate,
    iar timestampurile sunt garantat crescatoare pentru fiecare cheie.

    Asta inseamna ca putem pastra o lista simplă de perechi (valoare, timestamp)
    pentru fiecare cheie. Pentru a raspunde la o interogare de tip get(cheie, timestamp),
    trebuie doar sa gasim cel mai recent timestamp care este ≤ timestampul dat.
    Deoarece timestampurile sunt sortate, putem folosi cautarea binara pentru a
    gasi rapid aceasta pozitie, in loc sa scanam totul.

    O abordare eficienta si clara:
    stocarea valorilor in arrayuri (stocate intr un hash map) la set, apoi
    cautarea binara a timestampurilor la get.

    set: T = O(1)
    get: T = O(log n)
    space: S = O(n)
    """
    def __init__(self):
        self.store = collections.defaultdict(list)  # key: [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        left = 0
        right = len(values) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
