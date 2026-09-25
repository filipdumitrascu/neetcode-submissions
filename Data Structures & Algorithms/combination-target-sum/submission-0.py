class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        """Backtracking

        Vrem să generăm toate combinațiile de numere a căror sumă este egală cu
        valoarea țintă. Fiecare număr poate fi folosit de mai multe ori, așa că
        la fiecare index avem două opțiuni:
        -Să includem numărul curent, să rămânem la același index
        (deoarece îl putem reutiliza).
        -Să omitem numărul curent, să trecem la următorul indice.

        Explorăm toate opțiunile posibile folosind metoda backtracking.
        De fiecare dată când suma parțială este egală cu valoarea țintă, stocăm
        acea combinație.
        Dacă suma devine mai mare decât valoarea țintă sau rămânem fără numere,
        încetăm explorarea acelei căi.

        t - target, m - min(candidates)
        T = O(2^(t / m)), S = O(t / m)
        """
        # res = []

        # def dfs(i, cur, total):
        #     if total == target:
        #         res.append(cur.copy())
        #         return
        #     if i >= len(nums) or total > target:
        #         return

        #     cur.append(nums[i])
        #     dfs(i, cur, total + nums[i])
        #     cur.pop()
        #     dfs(i + 1, cur, total)

        # dfs(0, [], 0)
        # return res



        """Backtracking Optimal

        Această soluție optimizată de backtracking evită explorarea căilor
        inutile prin utilizarea sortării și a opririi timpurii.

        -Sortăm numerele astfel încât, odată ce un număr face ca suma să 
        depășească valoarea țintă, toate numerele care urmează după acesta vor
        depăși, de asemenea, valoarea țintă (putem opri în siguranță
        explorarea ulterioară (break / return) ).
        -La fiecare poziție, încercăm fiecare număr începând de la indexul i,
        permițând reutilizarea aceluiași număr.
        -Construim combinații pas cu pas și, ori de câte ori totalul curent este
        egal cu valoarea țintă, înregistrăm lista curentă.

        Sortarea combinată cu eliminarea combinărilor inutile(pruning) reduce
        semnificativ recursivitatea inutilă.

        t - target, m - min(candidates)
        T = O(2^(t / m)), S = O(t / m)
        """
        res = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()

        dfs(0, [], 0)
        return res
