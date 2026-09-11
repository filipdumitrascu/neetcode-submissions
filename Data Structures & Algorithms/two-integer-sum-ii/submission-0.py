class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """Brute Force   TLE

        Straightforward se ignora ca numerele sunt sortate si se veerifica
        fiecare pereche de 2 elemente. Daca suma acestora este egala cu target,
        pozitiile sunt returnate. Dar nu pentru asta a fost gandita problema
        intrucat nu se foloseste proprietatea de sortare sau alt trick.

        T = O(n^2), S = O(1)
        """
        # for i in range(len(numbers) - 1):
        #     for j in range(1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]
        # return []



        """Binary Search

        Deoarece arrayul este sortat, nu are sens sa verificam fiecare pereche.
        Pentru fiecare numar, stim de ce numar avem nevoie ca sa obtinem suma
        dorita: target - numar. Putem sa cautam acest complement prin binary search
        intre restul elelemtelor in loc de o scanare liniara. Astfel,
        searchul intern isi reduce complexitatea de la O(n) la O(log n),
        facand solutia mai rapida. N binary searches ==> O(n log n)

        T = O(n log n), S = O(1)
        """
        # for i in range(len(numbers)):
        #     left = i + 1
        #     right = len(numbers) - 1
        #     temp = target - numbers[i]

        #     while left <= right:
        #         mid = left + (right - left) // 2
        #         if numbers[mid] == temp:
        #             return [i + 1, mid + 1]

        #         if numbers[mid] < temp:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        
        # return []



        """Hash Map

        Solutia de la Two Sum 1 de a folosi un hash map ofera in continuare
        complexitate temporala O(n) si spatiala O(n) fara a folosi proprietatea
        ca elementele sunt sortate. Prin iterarea in array daca in hash map
        exista elementul de interes pentru cel curent: target - cel curent,
        atunci suma se poate realiza si sunt returnate pozitiile.

        T = O(n), S = O(n)
        """
        # num_to_index = {}
        # for index, num in enumerate(numbers):
        #     candidate = target - num

        #     if candidate in num_to_index:
        #         return [num_to_index[candidate] + 1, index + 1]
        #     num_to_index[num] = index

        # return []



        """Two Pointers

        Approachul care foloseste proprietatea ca elementele sunt sortate
        si se realizeaza in timp liniar dara spatiu auxiliar presupune utilizarea
        a doi pointeri, cel din stanga pe primul element iar cel din dreapta
        pe ultimul element. Cu ajutorul acestora suma poate fi ajustata:
        marind-o prin mutarea celui din stanga catre dreapta si micsorand-o
        prin mutarea celui din dreapta catre stanga. Nu se verifica orice pereche
        si se gasesc exact cele 2 numere dorite.

        T = O(n), S = O(1)
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            candidate = numbers[left] + numbers[right]

            if candidate == target:
                return [left + 1, right + 1]

            if candidate > target:
                right -= 1
            else:
                left += 1

        return []
