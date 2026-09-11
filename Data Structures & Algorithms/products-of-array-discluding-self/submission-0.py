class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """Brute Force    TLE

        O solutie straightforward este ca pentru fiecare pozitie din array,
        sa calculam produsul elementelor celorlalte pozitii din array.
        Extrem de ineficient pentru ca repeta o trecere completa prin array
        pentru fiecare element.

        T = O(n^2)
        S = O(1)
        """
        # result = [0] * len(nums)
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         product *= nums[j]

        #     result[i] = product
        # return result



        """Division    DENIED

        In timp liniar, smart ar fi fost sa impart produsul total la elementul
        curent dar impartirea este interzisa. (edge caseurile cu impartirea
        la 0 tratate)

        T = O(n), S = O(1)
        """
        # product = 1
        # zero_count = 0

        # for num in nums:
        #     if num:
        #         product *= num
        #     else:
        #         zero_count +=  1

        # if zero_count > 1:
        #     return [0] * len(nums)

        # result = [0] * len(nums)
        # for index, num in enumerate(nums):
        #     if zero_count:
        #         result[index] = 0 if num else product
        #     else:
        #         result[index] = product // num
        # return result



        """Prefix and Suffix

        Pentru fiecare indice, avem nevoie de produsul tuturor elementelor
        situate inaintea lui si al tuturor elementelor situate dupa el.
        In loc sa recalculam produsul in mod repetat, putem precalcula
        doua arrayuri utile:

        Produsul prefix: pref[i] = produsul tuturor elementelor din stanga lui i
        Produsul sufix: suff[i] = produsul tuturor elementelor din dreapta lui i
        Apoi, raspunsul final pentru fiecare indice este pur si simplu:
        result[i] = pref[i] x suff[i]

        T = O(n), S = O(n)
        """
        # result = [0] * len(nums)
        # pref = [0] * len(nums)
        # suff = [0] * len(nums)

        # pref[0] = 1
        # suff[len(nums) - 1] = 1

        # for i in range(1, len(nums)):
        #     pref[i] = nums[i - 1] * pref[i - 1]

        # for i in range(len(nums) - 2, -1, -1):
        #     suff[i] = nums[i + 1] * suff[i + 1]

        # for i in range(len(nums)):
        #     result[i] = pref[i] * suff[i]

        # return result



        """Prefix and Suffix (Optimal)

        Putem calcula produsul tuturor elementelor, cu excepția celui curent,
        fara a folosi arrayuri suplimentare de prefix si sufix.
        In schimb, reutilizam arrayul de rezultate si construim raspunsul in
        doua etape simple:

        In prima etapa, completam res[i] cu produsul tuturor elementelor aflate
        la stanga lui i (produs prefix).

        In a doua etapa, inmultim fiecare res[i] cu produsul tuturor elementelor
        aflate la dreapta lui i (produs postfix).

        Prin mentinerea a doua valori curente — prefix si postfix — evitam
        necesitatea unor tabele separate pref si suff.
        Astfel obtinem aceeasi logica ca in metoda anterioara, dar cu un
        spatiu suplimentar de complexitate O(1).

        T = O(n), S = O(1)
        """
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
