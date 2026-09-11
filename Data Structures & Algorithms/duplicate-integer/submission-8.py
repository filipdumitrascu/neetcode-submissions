class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        """Brute Force

        Cea mai intuitiva abordare este verificarea tuturor perechiilor de
        2 elemente si returnarea lui True, daca exista o pereche care are ambele
        valori egale. Este cea mai ineficienta abordare pentru ca examineaza
        fiecare pereche in parte.

        T = O(n^2), S = O(1)
        """
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False



        """Sorting

        Daca sortam arrayul, duplicatele se plaseaza unele langa altele. Astfel,
        este suficienta o singura trecere liniara printe elemente, comparand
        elementele adiacente.

        T = O(n log n), S = O(n)
        """
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i - 1] == nums[i]:
        #         return True
        # return False



        """Hash Set

        Putem folosi un hash set pentru a gasi eficient duplicatele. Pe masura ce
        iteram prin array, se cauta elementul curent daca exista si in hash set.
        Daca este inseamna ca l-am vazut si anterior si este duplicat. Hash setul
        are timp constat de cautare si ofera o solutie mult mai eficienta.

        T = O(n), S = O(n)
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False



        """Hash Set Length

        Hash Set ul pastreaza doar elemente unice in interior. Astfel, daca sizeul
        acestuia e mai mic stric ca sizeul arrayului, inseamna ca a eliminat din
        duplicate cand a fost creat.

        T = O(n), S = O(n)
        """
        # return len(set(nums)) < len(nums)
