import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """Linear Seach

        Problema consta in determinarea vitezei minime de banane per ora pe care
        trebuie sa o aiba koko pentru a manca toate pileurile pana in h ore.
        Astfel, ideea brute force o reprezinta incercarea liniara a tuturor
        vitezelor de la 1 pana la cantintate maxima pile si cand prima viteza
        a consumat toate pileurile in cel mult h ore, aceea e raspunsul.

        m - max(piles), n - len(piles)
        T = O(n * m), S = O(1)
        """
        # max_piles = max(piles)

        # for speed in range(1, max_piles + 1):
        #     hours_spent = 0

        #     for pile in piles:
        #         hours_spent += math.ceil(pile / speed)

        #     if hours_spent <= h:
        #         return speed

        # return max_piles



        """Binary Search (on answer)

        In loc sa incercam toate vitezele pe rand, putem sa cautam binar viteza
        cea mai mica (care mamanca in cel mult h ore toate pileurile). O viteza
        mai mare implica un timp total mai mic. Ca urmare se cauta in jumatatea
        cu viteze mai mari daca timpul e prea mare si invers.

        m - max(piles), n - len(piles)
        T = O(n log m), S = O(1)
        """
        left = 1
        right = max(piles)

        result = right
        while left < right:
            k = left + (right - left) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k)

            # if koko can eat all the bananas with 
            # this k, search a smaller k
            if hours <= h:
                result = min(result, k)
                right = k
            else:
                left = k + 1

        return result
