class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """Brute Force

        O secventa consecutiva se extinde prin verificarea existentei urmatorului
        numar (num + 1, num + 2, …) in multime. Un approach straightforward
        pornește pur si simplu de la fiecare numar din lista si incearca să
        extinda o serie consecutiva cat mai mult posibil.
        Pentru fiecare numar, verificam in mod repetat dacă numarul urmator exista,
        marind lungimea seriei pana cand secventa se intrerupe.
        Desi aceasta metoda functioneaza, ea implica eforturi repetate inutile,
        deoarece multe secvente sunt recalculate de mai multe ori.

        T = O(n^2), S = O(n)
        """
        # result = 0
        # store = set(nums)

        # for num in nums:
        #     streak = 0
        #     current = num

        #     while current in store:
        #         streak += 1
        #         current += 1
        #     result = max(result, streak)
        # return result


        """Sorting

        Daca sortam numerele mai intai, atunci toate valorile consecutive o sa
        apara unele langa altele. Devine usor sa navigam prin lista sortata si
        sa numaram cat de lunga este fiecare secventa consecutiva.

        Avansam cat timp numarul curent este egal cu valoarea expected in secventa
        Duplicatele nu afecteaza rezultatul, sunt skiped iar streakul nu se pierde.
        Acest approach e mai simplu si mai organizat decat solutia bruta pentru
        ca sortarea plaseaza potentialele secvente in ordine.

        T = O(n log n), S = O(n)
        """
        # if not nums:
        #     return 0
        
        # result = 0
        # nums.sort()

        # curr = nums[0]
        # streak = 0

        # i = 0
        # while i < len(nums):
        #     if curr != nums[i]:
        #         curr = nums[i]
        #         streak = 0

        #     while i < len(nums) and nums[i] == curr:  # skip duplicates
        #         i += 1
            
        #     streak += 1
        #     curr += 1
        #     result = max(result, streak)

        # return result


        """Hash Set

        Pentru a evita recalcularea aceleiasi secvente, trebuie inceputa 
        numararea secventei cand gasim inceputul unei secvente de numere 
        consecutive. Un numar este inceputulul unei secvente daca num - 1
        nu se afla in set (setul numerelor).

        Odata ce identificam un astfel de numar, pus si simplu cautam in set
        in timp constant existenta lui num + 1, num + 2 etc si extindem streakul
        cat de mult posibil. Astfel solutia se realizeaza in timp liniar pentu
        ca fiecare numar contribuie doar o singura data la secvente.

        T = O(n), S = O(n)
        """
        num_set = set(nums)
        result = 0

        for num in num_set:
            if num - 1 in num_set:
                continue

            length = 1
            while num + length in num_set:
                length += 1

            result = max(result, length)

        return result
