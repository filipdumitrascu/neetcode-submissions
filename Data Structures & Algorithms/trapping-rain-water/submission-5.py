class Solution:
    def trap(self, height: list[int]) -> int:
        """Brute Force    TLE

        Pentru fiecare pozitie, cantitatea de apa stocata depinde de cea mai
        inalta bara din stanga si cea mai inalta din dreapta. Daca stim aceste
        doua valori, apa la indexul i se caculeaza prin minimul dintre ele - 
        inaltimea barii de pe pozitia curenta.

        Practic, problema se reduce la a calcula maximul din stanga si minimul
        din dreapta pentru fiecare pozitie. Brute force o facem pentru fiecare
        inaltime. Ineficient dar obtinem rezultatul corect.

        T = O(n^2), S = O(1)
        """
        # if not height:
        #     return 0

        # result = 0
        # for i in range(len(height)):
        #     left_max = height[i]
        #     right_max = height[i]

        #     for j in range(i):
        #         left_max = max(left_max, height[j])
        #     for j in range(i + 1, len(height)):
        #         right_max = max(right_max, height[j])

        #     result += min(left_max, right_max) - height[i]

        # return result



        """Prefix and Suffix

        In loc sa calculam de fiecare data maximul stanga dreapta, putem sa le
        calculam o singura data. Construim doi array:
        left_max[i] = cea mai inalta bara de la inceput pana in indexul i.
        right_max[i] = cea mai inalta bara de la indexul i pana la sfarsit.

        Astfel, atat constructia cat si calculul apei se pot face in timp liniar
        folosind acest spatiu auxiliar.

        T = O(n), S = O(n)
        """
        # n = len(height)
        # if not height:
        #     return 0

        # left_max = [0] * n
        # right_max = [0] * n

        # left_max[0] = height[0]
        # for i in range(1, n):
        #     left_max[i] = max(left_max[i - 1], height[i])

        # right_max[n - 1] = height[n - 1]
        # for i in range(n - 2, -1, -1):
        #     right_max[i] = max(right_max[i + 1], height[i])

        # result = 0
        # for i in range(n):
        #     result += min(left_max[i], right_max[i]) - height[i]

        # return result



        """Two Pointers

        Apa la orice pozitie depinde de bara mai scurta din partea stanga si dreapta.
        Astfel daca bara maxima din stanga e mai mica ca cea din dreapta, nici
        nu conteaza ce inaltime are exact cea din dreapta, e clar ca cea din
        stanga ajuta la calculul apeii pe pozitia curenta. Putem sa mutam pointerul
        din stanga spre centru sigur, calculand cat de multa apa poate fi pusa
        pe pozitia corecta. Similar pentru pointerul drept.

        Pe masura ce avanseaza pointerii, tinem cont de cea mai inalta bara
        vazuta si pe stanga si pe dreapta. Astfel, apa se calculeza usor:
        max bar pe partea curenta - inaltimea pla pozitia curenta.

        In acest fel, calculam apa treptat cu 2 ponteri cand de pe partea stanga
        cand de pe partea dreapta, asigurand mereu ca lucram cu minimul dintre
        maximul pe stanga si cel pe dreapta. Acesta abordare reduce complexitatea
        spatiala la O(1).

        T = O(n), S = O(1)
        """
        if not height:
            return 0

        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]
        result = 0

        while left < right:
            # shift the smaller pointer (left or right)
            # and use it s max (which is smaller) to calculate the area
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                result += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                result += right_max - height[right]
        return result
