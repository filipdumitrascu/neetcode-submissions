class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """Brute Force

        Abordarea de tip „brute-force” încearcă fiecare submulțime posibilă a
        numerelor candidate. 
        -Sortăm arrayul astfel încât combinațiile duplicate să apară în aceeași
        ordine.
        -La fiecare indice, avem două opțiuni:
            -Să includem numărul curent.
            -Să omitem numărul curent.
        -Astfel se generează toate submulțimile (asemănător unui arbore binar
        de opțiuni).
        -De fiecare dată când suma unui subset este egală cu valoarea țintă,
        îl stocăm.
        -Pentru a evita combinațiile duplicate, stocăm fiecare rezultat sub
        forma unui tuple într-un set.

        Această metodă este ușor de înțeles, dar lentă, deoarece explorează
        toate subseturile, chiar și pe cele nevalide sau duplicate.

        T = O(n * 2^n), S = O(n * 2^n)
        """
        # res = set()
        # candidates.sort()

        # def generate_subsets(i, cur, total):
        #     if total == target:
        #         res.add(tuple(cur))
        #         return
        #     if total > target or i == len(candidates):
        #         return

        #     cur.append(candidates[i])
        #     generate_subsets(i + 1, cur, total + candidates[i])
        #     cur.pop()

        #     generate_subsets(i + 1, cur, total)

        # generate_subsets(0, [], 0)
        # return [list(combination) for combination in res]



        """Backtracking

        Scopul este de a alege numere a căror sumă să fie egală cu valoarea
        țintă, dar fiecare număr poate fi folosit o singură dată, iar lista
        poate conține duplicate.
        Pentru a evita generarea de combinații duplicate, procedăm astfel:
        -Sortăm matricea astfel încât duplicatele să apară unul lângă altul.
        -Folosim metoda backtracking pentru a explora opțiunile:
            -Luăm numărul curent.
            -Sărim peste numărul curent.
        -Când sărim, omitem toate duplicatele dintr-o singură mișcare pentru a
        evita crearea de combinații duplicate precum [1,2,2] de mai multe ori.
        -Dacă suma parțială depășește valoarea țintă, încetăm explorarea căii
        curente înainte de timp.
        
        Sortarea + omiterea duplicatelor + backtrackingul ne asigură că
        construim doar combinații valide și unice.

        T = O(n* 2^n), S = O(n)
        """
        # res = []
        # # this way a loop can skip adjacent values in order not
        # # to create duplicate combinations
        # candidates.sort()


        # def bkt(i, cur, total):
        #     # same cases as problem i
        #     if total == target:
        #         res.append(cur.copy())
        #         return

        #     if total > target or i == len(candidates):
        #         return

        #     cur.append(candidates[i])
        #     bkt(i + 1, cur, total + candidates[i])  # left branch, include candidate
        #     cur.pop()

        #     while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
        #         i += 1
        #     bkt(i + 1, cur, total)  # right branch, include no occurence of candidate

        # bkt(0, [], 0)
        # return res



        """Backtracking Optimal

        Avem nevoie de toate combinațiile unice în care fiecare număr poate
        fi folosit cel mult o singură dată, iar numerele duplicate din datele
        de intrare nu trebuie să genereze combinații duplicate.

        Pentru a gestiona în siguranță numerele duplicate, procedăm astfel:
        -Sortăm tabloul
        Astfel, numerele egale sunt grupate împreună, ceea ce ne ajută să
        omitem cu ușurință duplicatele.
        -Folosim metoda backtracking, în care, la fiecare indice, decidem:
            -Să luăm numărul
            -Să omitem numărul
        -Pentru a evita combinațiile duplicate:
            -Dacă candidates[i] == candidates[i - 1] și ne aflăm încă la
            același nivel de recursivitate (i > idx), sărim peste acel număr.
        -Ne oprim mai devreme dacă current_sum + candidates[i] > target,
        deoarece lista este sortată.

        Această abordare explorează fiecare număr o singură dată pe fiecare
        cale de combinație și garantează că nu vor exista rezultate repetate.

        T = O(n * 2^n), S = O(n)
        """
        res = []
        candidates.sort()

        def dfs(idx, path, cur):
            if cur == target:
                res.append(path.copy())
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if cur + candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(i + 1, path, cur + candidates[i])
                path.pop()

        dfs(0, [], 0)
        return res
