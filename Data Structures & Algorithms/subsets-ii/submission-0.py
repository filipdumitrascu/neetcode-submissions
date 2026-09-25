class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        """Brute Force

        Această metodă de tip „brute-force” generează fiecare subset posibil,
        efectuând o alegere binară la fiecare index:
        -Includerea numărului curent sau
        -Omiterea numărului curent.

        Deoarece există duplicate, multe dintre subseturile generate pot părea
        identice. Pentru a evita returnarea duplicatelor, procedăm astfel:
        -Mai întâi sortăm tabloul, astfel încât duplicatele să fie una lângă alta.
        -Stocăm fiecare submulțime ca un tuple în interiorul unui set, deoarece:
        Seturile elimină automat duplicatele.
        Tuple-urile sunt hashabile (listele nu sunt).
        În final, convertim setul de tuple înapoi într-o listă de liste.

        T = O(n * 2^n), S = O(2^n)
        """
        # res = set()

        # def backtrack(i, subset):
        #     if i == len(nums):
        #         res.add(tuple(subset))
        #         return

        #     subset.append(nums[i])
        #     backtrack(i + 1, subset)
        #     subset.pop()
        #     backtrack(i + 1, subset)

        # nums.sort()
        # backtrack(0, [])
        # return [list(s) for s in res]



        """Backtracking I

        Vrem toate submulțimile, dar matricea poate conține elemente duplicate.
        Dacă generăm orbește toate submulțimile, vom obține unele repetate.
        Așadar, trebuie să evităm alegerea aceleiași valori la același nivel de
        decizie de mai multe ori.

        Ideea cheie:
        -La fiecare indice i, facem două alegeri:
            -Includem nums[i]
            -Excludem nums[i]
        
        Însă, atunci când excludem, dacă numărul următor este același
        (nums[i] == nums[i+1]), atunci omiterea lui acum și omiterea lui mai
        târziu duc la același subset.
        Așadar, după ce explorăm ramura „excludere”, omitem toate valorile
        duplicate pentru a evita generarea de subseturi duplicate.

        De asemenea, sortăm mai întâi tabloul, astfel încât duplicatele să
        devină consecutive și ușor de omis.

        T = O(n * 2^n), S = O(n)
        """
        # res = []
        # nums.sort()

        # def backtrack(i, subset):
        #     if i == len(nums):
        #         res.append(subset[::])
        #         return

        #     subset.append(nums[i])
        #     backtrack(i + 1, subset)
        #     subset.pop()

        #     while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        #         i += 1
        #     backtrack(i + 1, subset)

        # backtrack(0, [])
        # return res



        """Backtracking II

        Vrem să generăm toate submulțimile, dar duplicatele din datele de
        intrare pot duce la apariția unor submulțimi repetate.
        Pentru a evita duplicatele în mod eficient, în loc să luăm decizii de
        tipul „alege / nu alege”, această abordare construiește submulțimi
        alegând fiecare element următor posibil — dar doar o singură dată
        pentru fiecare valoare unică la fiecare nivel de recursivitate.

        Ideea cheie:
        -Sortăm arrayul astfel încât numerele identice să fie unul lângă altul.
        -La fiecare nivel de recursivitate, parcurgem în buclă variabila j de
        la indexul curent până la sfârșit.
        -Dacă nums[j] este identic cu nums[j-1] și j > i, îl omitem.
        Acest lucru împiedică generarea aceluiași subset care începe cu același
        prefix.
        -De fiecare dată când intrăm în backtrack, adăugăm submulțimea
        curentă în res.

        Acest lucru asigură:
        -Fiecare submulțime este generată exact o singură dată.
        -Toate submulțimile valide sunt incluse.
        -Nu este nevoie de mulțimi sau structuri de date suplimentare.

        T = O(n * 2^n), S = O(n)
        """
        # nums.sort()
        # res = []
        # def backtrack(i, subset):
        #     res.append(subset[::])

        #     for j in range(i, len(nums)):
        #         if j > i and nums[j] == nums[j - 1]:
        #             continue
        #         subset.append(nums[j])
        #         backtrack(j + 1, subset)
        #         subset.pop()

        # backtrack(0, [])
        # return res



        """Iteration

        Această metodă iterativă construiește submulțimi pas cu pas.
        În mod normal, fiecare număr nou este adăugat la toate submulțimile
        existente. Însă duplicatele duc la apariția unor submulțimi repetate —
        așa că trebuie să evităm recombinarea duplicatelor cu toate
        submulțimile anterioare.

        Ideea cheie:
        -Sortăm arrayul astfel încât duplicatele să fie una lângă alta.
        -Mențineți doi indici:
            -idx: punctul de pornire pentru generarea de noi submulțimi.
            -prev_idx: punctul final (dimensiunea anterioară a listei de
            rezultate înainte de adăugarea acestui număr).
        -Dacă numărul curent nu este un duplicat, începem de la început
        (idx = 0).
        -Dacă este un duplicat, îl combinăm doar cu submulțimile create în
        ultima rundă.
        Astfel se evită generarea de submulțimi duplicate.

        Exemplu:
        Pentru intrarea [1,2,2]
        -Primul 2 extinde toate submulțimile.
        -Al doilea 2 extinde doar submulțimile adăugate la procesarea
        primului 2 → fără duplicate.

        T = O(n * 2^n), S = O(1)
        """
        nums.sort()
        res = [[]]
        prev_idx = 0
        idx = 0

        for i in range(len(nums)):
            idx = prev_idx if i >= 1 and nums[i] == nums[i - 1] else 0
            prev_idx = len(res)

            for j in range(idx, prev_idx):
                tmp = res[j].copy()
                tmp.append(nums[i])
                res.append(tmp)

        return res
