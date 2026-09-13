class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Binary Search Recursive

        Cautarea binarea functioneaza prin a taia in jumatate repetitiv
        multimea de elemente. In loc sa cuatam liniar prun tot arrayul,
        ne uitam la elementul din mijloc si in funcite de el:
         daca e elementul dorit, returnam indexul
         daca e mai mare decat elementul dorit, ne ducem in jumatatea stanga
          (unde sunt elemente mai mici ca sa il gasim pe cel dorit)
         daca e mai mic decat elementul dorit, ne ducem in jumatatea dreapta
          (unde sunt elemente mai mari ca sa il gasim pe cel dorit)
        De precizat ca arrayul trebuie sa fie sortat pentru ca sa se garanteze
        aceasta cautare

        Versiunea recursiva foloseste aceasta idee, apelandu se pe jumatatea
        care trebuie pana se gaseste targetul. Timpul este logaritmic.

        T = O(log n), S = O(log n)
        """
        # def bin_search(left: int, right: int) -> int:
        #     if left >= right:
        #         return -1

        #     mid = left + (right - left) // 2

        #     if nums[mid] == target:
        #         return mid

        #     if nums[mid] < target:
        #         return bin_search(mid + 1, right)
        #     return bin_search(left, mid)

        # return bin_search(0, len(nums))



        """Binary Search Iterative

        Varianta iterativa foloseste doi pointeri care sunt modificati intr-un
        loop. Daca pointerii vin unul peste celalalt, nu s a gasit elementul.

        T = O(log n), S = O(1)
        """
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return -1


        # import bisect
        # index = bisect.bisect_left(nums, target)
        # return index if index < len(nums) and nums[index] == target else -1
