class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """Backtracking

        Ideea este de a construi toate submulțimile posibile, făcând o alegere
        la fiecare pas: pentru fiecare număr, avem două opțiuni — să-l includem
        sau să-l excludem.
        Astfel se formează în mod natural un arbore de decizie.

        Metoda backtracking ne ajută să explorăm ambele opțiuni:
        -Adăugăm numărul curent → continuăm explorarea
        -Îl eliminăm (anulăm) → explorăm fără el

        De fiecare dată când ajungem la capătul arrayului, lista curentă
        reprezintă un subset complet, așa că îl stocăm.
        Astfel se generează sistematic toate cele 2ⁿ subseturi.

        T = O(n * 2^n), S = O(n)
        """
        res = []
        subset = []

        def bkt(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            bkt(i + 1)

            # decision not to include nums[i]
            subset.pop()
            bkt(i + 1)

        bkt(0)
        return res
