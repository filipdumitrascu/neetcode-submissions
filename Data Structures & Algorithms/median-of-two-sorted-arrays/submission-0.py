class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """Merge Sort    TLE

        Cea mai simpla metoda de a afla mediana a doua arrayuri sortate este sa
        le combinam intr-un singur tabel si apoi sa-l sortam. Odata ce totul
        este combinat si sortat, gasirea medianei devine simpla:
        Daca numarul total de elemente este impar → elementul din mijloc este
        mediana. Daca este par → mediana este media celor doua elemente din
        mijloc. Aceasta metodă este usor de inteles, dar nu profita de
        faptul ca arrayurile de intrare sunt deja sortate.

        m - len(nums1), n - len(nums2)
        T = O(m + n), S = O(1)
        """
        # i = 0
        # j = 0
        # median1 = 0
        # median2 = 0

        # for _ in range((len(nums1) + len(nums2)) // 2 + 1):
        #     median2 = median1
        #     if i < len(nums1) and j < len(nums2):
        #         if nums1[i] > nums2[j]:
        #             median1 = nums2[j]
        #             j += 1
        #         else:
        #             median1 = nums1[i]
        #             i += 1
        #     elif i < len(nums1):
        #         median1 = nums1[i]
        #         i += 1
        #     else:
        #         median1 = nums2[j]
        #         j += 1

        # return float(median1) if (len(nums1) + len(nums2)) % 2 else (median1 + median2) / 2.0



        """Binary search on the smaller array

        Vrem sa aflam mediana a doua arrayuri sortate fara a le uni complet.
        Imaginati-va ca asezati cele doua arrayuri unul langa celalat si faceti
        o taietura (partitie) astfel incat:
        -Partea stanga a taieturii sa contina exact jumatate din numarul total
        de elemente (sau jumatate + 1, daca numarul este impar).
        -Toate elementele din partea stanga sunt <= toate elementele din partea
        dreapta.

        Daca putem gasi o astfel de partitie, atunci:
         Mediana trebuie sa provina de la elementele de la marginea acestei
        taieturi:
         -cel mai mare element din partea stanga,
         -si cel mai mic element din partea dreapta.
        Pentru a gasi aceasta taietura in mod eficient, procedam astfel:
        -Efectuam cautarea binara doar pe arrayul mai mic.
        -Pentru o taietura aleasa in arrayul mai mic, taietura din arrayul mai
         mare este fixa (astfel incat numarul total de elemente din stanga sa
         fie jumatate).
        -Verificam daca aceasta partitie este valida:
          a_left <= b_right și b_left <= a_right
         -Daca nu este valida:
           Deplasam linia de separare spre stanga sau spre dreapta (ca în cazul
           unei căutari binare obisnuite) pana cand devine valida.
        Odată ce avem o partitie valida, calculam mediana folosind valoarea
        maxima din partea stanga si valoarea minima din partea dreapta.

        T = O(log(m + n)), S = O(1)
        """
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(b) < len(a):
            a, b = b, a

        left, right = 0, len(a) - 1

        while True:
            i = left + (right - left) // 2  # a
            j = half - i - 2  # b

            a_left = a[i] if i >= 0 else float("-infinity")
            a_right = a[i + 1] if (i + 1) < len(a) else float("infinity")

            b_left = b[j] if j >= 0 else float("-infinity")
            b_right = b[j + 1] if (j + 1) < len(b) else float("infinity")

            # partitions are correct (if appended result in a sorted array)
            if a_left <= b_right and b_left <= a_right:
                # odd
                if total % 2:
                    return min(a_right, b_right)

                # even
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            
            elif a_left > b_right:
                right = i - 1
            else:
                left = i + 1
