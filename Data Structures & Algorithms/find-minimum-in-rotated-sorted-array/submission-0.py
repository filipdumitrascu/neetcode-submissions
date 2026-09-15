class Solution:
    def findMin(self, nums: list[int]) -> int:
        """Linear Search

        Un rotated sorted array tot contine toate valorile originale, dar altfel
        pozitionate. Astfel, cea mai simpla rezolvare este sa cautam liniar prin
        tot arrayul minimul fara sa ne gandim la ce ar putea sa insemne aceasta
        rotatie intre elemente.

        T = O(n), S = O(1)
        """
        # return min(nums)



        """Binary Search

        Un rotated array sortat are o proprietate speciala:
        - Prima parte a lui are valorile mai mari. (o notam A)
        - A doua parte incepe cu minimul si are valorile mai mici. (o notam B)
        (Bine, mai exista edge caseul in care nu e rotit, e pur
        si simplu sortat cresctator.)

        Putem folosi cautare binara pentru a identifica unde e minimul:
        - Daca midul este mai mare decat left, inseamna ca midul e ales in
        prima parte (A), ca urmare ne ducem in a doua jumate (pentru a doua parte
        a arrayului, unde e minimul)
        - Altfel, midul e mai mic decat left, ca urmare midul e ales in a doua
        parte (B), ca urmare ne ducem in prima jumate pentru ca e posibil ca
        minimul sa fie inainte de mid, unde incepe B si se termina A.

        T = O(log n), S = O(1)
        """
        result = float("inf")
        left = 0
        right = len(nums) - 1

        while left <= right:
            # left and right are in a sorted part
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break

            mid = left + (right - left) // 2
            result = min(result, nums[mid])

            # Knowing that a rotated array has greater values in the first part,
            # if mid is in the first part, search the second part
            if nums[left] <= nums[mid]:
                left = mid + 1

            # if not, even if mid is in the second part, in which there are the
            # smaller elements, mid can be greater than a right elem, also in
            # the second part
            else:
                right = mid - 1

        return result
