class Solution:
    def maxArea(self, heights: list[int]) -> int:
        """Brute Force    TLE

        Se incearca toate perechile de inaltimi si se calculeaza aria pe care
        o formeaza. Aria se calculeaza ca minimul dintre cele 2 inaltimi de
        inmultit cu latimea dintre cele doua inaltimi. Se garanteaza ca se
        gaseste aria maxima dar e o solutie ineficienta

        T = O(n^2), S = O(1)
        """
        # result = 0
        # for i in range(len(heights) - 1):
        #     for j in range(i + 1, len(heights)):
        #         result = max(result, min(heights[i], heights[j]) * (j - i))
        # return result



        """Two Pointers

        Pentru o arie maxima se doresc cea mai mare latime si cea mai mare
        inaltime. Plecam cu latimea maxima, calculand aria pentru prima si ultima
        inaltime, cate un pointer left si right. Inaltimea este limitata de 
        linia mai scurta, astfel pentru a incerca sa marim aria trebuie sa mutam
        pointerul de pe linia mai scurta catre centru. In acest fel, exploram
        in timp liniar toate posibilitatile care au sens si gasim aria maxima.

        T = O(n), S = O(1)
        """
        left = 0
        right = len(heights) - 1
        result = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            result = max(result, area)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return result
