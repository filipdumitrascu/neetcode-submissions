class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Brute Force

        Putem incerca fiecare pereche din array si sa returnam prima pereche
        care insumata da target. E cea mai intuitiva solutie dar si cea mai 
        ineficienta.

        T = O(n^2), S = O(1)
        """
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []



        """Sorting

        O singura trecere prin array ar fi mai eficienta decat solutia brute force.
        Astfel, sortam elementele crescator si fixam 2 pointeri, unul pe primul
        si celalalt pe ultimul element. Fiind sortate stim clar: Daca vreau sa
        maresc suma mut primul pointer catre dreapta iar daca vreau sa o micsorez,
        mut al doilea pointer catre stanga. Astfel, se garanteaza gasirea
        celor 2 elemente care dau exact suma target in timp liniar. Singurul
        bottleneck este sortarea.

        T = O(n log n), S = O(n)
        """
        # indexed_nums: list[tuple[int, int]] = []

        # for index, num in enumerate(nums):
        #     indexed_nums.append((num, index))

        # indexed_nums.sort(key=lambda pair: pair[0])

        # left = 0
        # right = len(indexed_nums) - 1

        # while left < right:
        #     candidate = indexed_nums[left][0] + indexed_nums[right][0]

        #     if candidate == target:
        #         if indexed_nums[left][1] < indexed_nums[right][1]:
        #             return [indexed_nums[left][1], indexed_nums[right][1]]
        #         return [indexed_nums[right][1], indexed_nums[left][1]]

        #     if candidate < target:
        #         left += 1
        #     else:
        #         right -= 1

        # return []



        """Hash Map

        Se declara un hash map care mapeaza elementul la pozitia lui in array.
        La iterarea prin array, se cauta in timp constant in aceasta structura
        de date daca complementul (adica elementul de care ar fi nevoie ca adunat
        cu elementul curent sa rezulte suma target) a fost anterior in array.
        In caz afirmativ se returneaza pozitiile.

        T = O(n), S = O(n)
        """
        num_to_index = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in num_to_index:
                return [num_to_index[complement], index]

            num_to_index[num] = index

        return []
