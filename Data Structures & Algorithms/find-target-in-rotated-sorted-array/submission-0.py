class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Brute Force

        Un rotated sorted array tot contine toate valorile originale, dar altfel
        pozitionate. Astfel, cea mai simpla rezolvare este sa cautam liniar prin
        tot arrayul minimul fara sa ne gandim la ce ar putea sa insemne aceasta
        rotatie intre elemente.

        T = O(n), S = O(1)
        """
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1



        """Binary Search

        Un rotated array sortat are o proprietate speciala:
        - Prima parte a lui are valorile mai mari. (o notam A)
        - A doua parte incepe cu minimul si are valorile mai mici. (o notam B)
        (Bine, mai exista edge caseul in care nu e rotit, e pur
        si simplu sortat cresctator.)

        Putem folosi cautare binara pentru a identifica pozitia lui target.
        Daca mid este mai mare decat left, inseamna ca mid este in prima
        parte a arrayului (A) iar daca este mai mic, este in a doua (B).
        Acum ca sitm partea in care se alfa, putem sa ajutam compararea lui target
        cu mid prin acest capat (left sau right). 
        - left < target < mid, automat target e in stanga de mid (mid = right - 1)
        - mid < target < right, automat target e in dreapta de mid (mid = left + 1)

        Chiar si cu arrayul rotit, elminam mereu jumatatea in care elemntul nu
        se afla si ajungem in timp logaritmic la rezultat.

        T = O(log n), S = O(1)
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
