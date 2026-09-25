class Solution:
    def partition(self, s: str) -> list[list[str]]:
        """Backtracking

        Vrem să împărțim șirul în segmente, dar păstrăm o împărțire doar dacă
        fiecare segment este un palindrom.

        Gândiți-vă la plasarea unor „tăieturi” în șir:
        -Începeți de la un anumit indice j (începutul următoarei porțiuni).
        -Încercați să extindeți indicele final i pentru a forma un subșir s[j..i].
        -Dacă s[j..i] este un palindrom, îl alegem (îl includem în porțiune) și
        apoi reluăm de la următoarea poziție (i+1) pentru a construi următoarea
        porțiune.
        -Indiferent dacă a fost sau nu un palindrom, putem, de asemenea, să
        extindem mai departe mutând i la i+1 (încercând un subșir mai lung
        pornind de la același început j).

        Backtracking înseamnă:
        -Când alegem o porțiune palindromică, mergem mai adânc.
        -După întoarcere, eliminăm acea porțiune și încercăm alte posibilități.

        T = O(n * 2^n), S = O(n)
        """
        res, part = [], []

        def is_pali(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left + 1, right - 1
            return True

        def dfs(j, i):
            if i >= len(s):
                if i == j:
                    res.append(part.copy())
                return

            if is_pali(s, j, i):
                part.append(s[j: i + 1])
                dfs(i + 1, i + 1)
                part.pop()

            dfs(j, i + 1)

        dfs(0, 0)
        return res
