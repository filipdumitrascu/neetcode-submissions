class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """Recursion

        Ideea este de a genera permutări prin alcătuirea lor din permutări mai
        mici.
        -Dacă lista este goală → singura permutare este [].
        -În caz contrar:
            -Se ia primul număr din listă.
            -Se obțin recursiv toate permutările numerelor rămase.
            -Pentru fiecare permutare mai mică, inserați primul număr în
            fiecare poziție posibilă.

            Exemplu:
            Dacă permutarea mai mică = [2,3] și numărul nou = 1,
            creăm: [1,2,3], [2,1,3], [2,3,1].

        Acest lucru funcționează deoarece inserarea numărului nou în toate
        pozițiile ne asigură că construim toate permutările unice.

        T = O(n! * n^2), S = O(n! * n)
        """
        # if len(nums) == 0:
        #     return [[]]

        # perms = self.permute(nums[1:])
        # res = []
        # for p in perms:
        #     for i in range(len(p) + 1):
        #         p_copy = p.copy()
        #         p_copy.insert(i, nums[0])
        #         res.append(p_copy)
        # return res



        """Iteration

        Construim permutări pas cu pas, folosind iterația în locul
        recursivității.
        Începem cu o permutare goală: [].
        Pentru fiecare număr din nums, luăm toate permutările existente și
        inserăm noul număr în fiecare poziție posibilă.

        Exemplu de proces de construire pentru [1,2,3]:
        -Început: []
        -Inserăm 1 → [1]
        -Insertăm 2 în fiecare poziție din [1] → [2,1], [1,2]
        -Insertăm 3 în fiecare poziție a fiecărei permutări:
            -Pentru [2,1] → [3,2,1], [2,3,1], [2,1,3]
            -Pentru [1,2] → [3,1,2], [1,3,2], [1,2,3]
        Prin inserarea fiecărui număr în toate pozițiile tuturor permutărilor
        existente, generăm toate permutările posibile.

        T = O(n! * n^2), S = O(n! * n)
        """
        # perms = [[]]
        # for num in nums:
        #     new_perms = []
        #     for p in perms:
        #         for i in range(len(p) + 1):
        #             p_copy = p.copy()
        #             p_copy.insert(i, num)
        #             new_perms.append(p_copy)
        #     perms = new_perms
        # return perms



        """Backtracking
        Metoda backtracking-ului construiește permutări alegând numerele unul
        câte unul și explorând toate ordonările posibile.

        La fiecare pas:
        -Alegem un număr care nu a fost încă folosit.
        -Îl adăugăm la permutarea curentă.
        -Continuăm generarea în mod recursiv.
        -Când ajungem la o permutare completă (lungime == len(nums)), o salvăm.
        -Apoi anulăm ultima alegere (backtracking) și încercăm un alt număr.

        Folosim un tablou pick pentru a marca elementele deja utilizate,
        asigurându-ne că fiecare număr apare o singură dată în fiecare permutare.

        Această metodă explorează un arbore de decizie în care fiecare nivel
        alege următorul număr până când toate numerele sunt utilizate.

        T = O(n! * n), S = O(n! * n)
        """
        # def backtrack(perm: list[int], nums: list[int], pick: list[bool]):
        #     nonlocal res

        #     if len(perm) == len(nums):
        #         res.append(perm[:])
        #         return

        #     for i in range(len(nums)):
        #         if not pick[i]:
        #             perm.append(nums[i])
        #             pick[i] = True

        #             backtrack(perm, nums, pick)
        #             perm.pop()

        #             pick[i] = False

        # res = []
        # backtrack([], nums, [False] * len(nums))
        # return res



        """Backtracking (Bit Mask)
        Vrem să generăm toate permutările, dar în loc să folosim un tablou
        boolean de pick, folosim o mască de biți (mask) pentru a ține evidența
        elementelor din nums care au fost utilizate.

        -Fiecare bit din mask indică dacă un indice i este utilizat.
        -Exemplu cu 4 numere:
            -mask = 0101 înseamnă că indicii 0 și 2 sunt deja aleși.
        Astfel, verificarea utilizării se face extrem de rapid folosind:
            -(mask & (1 << i)) → verifică dacă indicele i este utilizat.
            -(mask | (1 << i)) → marchează indicele i ca fiind utilizat
            pentru următorul apel recursiv.

        Construim permutările încercând fiecare indice neutilizat la fiecare
        pas, până când am ales toate numerele.

        T = O(n! * n), S = O(n! * n)
        """
        # def backtrack(perm: list[int], nums: list[int], mask: int):
        #     nonlocal res

        #     if len(perm) == len(nums):
        #         res.append(perm[:])
        #         return

        #     for i in range(len(nums)):
        #         if not (mask & (1 << i)):
        #             perm.append(nums[i])
        #             backtrack(perm, nums, mask | (1 << i))
        #             perm.pop()

        # res = []
        # backtrack([], nums, 0)
        # return res





        """Backtracking (Optimal)
        Această abordare generează permutări pe loc prin schimbarea între ele
        a elementelor. În loc să creăm liste noi sau să ținem evidența
        elementelor vizitate, tratăm matricea ca fiind împărțită în:
        -Prefix fix (pozițiile de la 0 la idx - 1)
        -Sufix liber (pozițiile de la idx până la sfârșit)

        La fiecare pas:
        -Alegem elementul care trebuie plasat în poziția idx.
        -Facem acest lucru schimbând între ele fiecare element i ≥ idx cu idx.
        -După plasarea unui număr în poziția idx, completăm recursiv următorul
        indice.
        -Când recursiunea se încheie, facem schimbul înapoi pentru a restabili
        lista inițială (backtracking).

        Aceasta generează toate permutările în mod eficient și utilizează un 
        spațiu suplimentar de ordinul O(1) (în afară de recursiune).

        T = O(n! * n), S = O(n! * n)
        """
        def backtrack(nums: list[int], idx: int):
            nonlocal res

            if idx == len(nums):
                res.append(nums[:])
                return

            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(nums, idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]

        res = []
        backtrack(nums, 0)
        return res
