import collections


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """Brute Force (Backtracking)

        Pentru fiecare celulă, încercăm să vedem încotro poate curge apa dacă
        pornește de acolo. Regulă: apa poate curge dintr-o celulă către una
        vecină numai dacă înălțimea celulei vecine este <= înălțimea curentă
        (în pantă sau pe teren plat).

        Așadar, pentru fiecare (r, c):
        - Se execută DFS explorând toate căile care continuă către înălțimi
        egale sau mai mici.
        - Dacă în timpul DFS ieșim vreodată din grilă:
            - Ieșire din limita de sus/stânga ⇒ apa poate ajunge în Pacific.
            - Ieșire din limita de jos/dreapta ⇒ apa poate ajunge în Atlantic.
        - Dacă ambele oceane sunt accesibile, includeți (r, c) în răspuns.

        -Pentru a evita buclele infinite, marcăm temporar celula curentă
        ca vizitată (aici, setând-o la inf) în timpul explorării, apoi o
        restabilim după revenire.

        m - rows, n - cols
        T = O(m * n * 4^(m * n)), S = O(m * n)
        """
        # rows, cols = len(heights), len(heights[0])
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # pacific = False
        # atlantic = False

        # def dfs(r, c, prev_val):
        #     nonlocal pacific, atlantic
        #     if r < 0 or c < 0:
        #         pacific = True
        #         return
        #     if r >= rows or c >= cols:
        #         atlantic = True
        #         return
        #     if heights[r][c] > prev_val:
        #         return

        #     tmp = heights[r][c]
        #     heights[r][c] = float('inf')
        #     for dx, dy in directions:
        #         dfs(r + dx, c + dy, tmp)
        #         if pacific and atlantic:
        #             break
        #     heights[r][c] = tmp

        # res = []
        # for r in range(rows):
        #     for c in range(cols):
        #         pacific = False
        #         atlantic = False
        #         dfs(r, c, float('inf'))
        #         if pacific and atlantic:
        #             res.append([r, c])
        # return res



        """DFS

        În loc să pornim DFS din fiecare celulă (proces lent), inversăm modul
        de gândire:

        O celulă poate ajunge la ocean dacă apa poate curge din acea celulă
        către ocean (în pantă/pe teren plat). Inversăm procesul: pornim de la
        marginile oceanului și ne deplasăm în sus pe pantă/pe teren plat
        (către celulele vecine cu altitudine >= cea curentă). Dacă poți urca
        de la ocean către o celulă, atunci acea celulă poate curge în jos
        către oceanul respectiv.

        Așadar, efectuăm 2 iterații DFS:
        - De la toate celulele de la marginea Pacificului (rândul de sus +
        coloana din stânga) → marcăm toate celulele accesibile din pac
        - De la toate celulele de la marginea Atlanticului (rândul de jos +
        coloana din dreapta) → marcăm toate celulele accesibile din atl

        Răspunsul = celulele care se află în ambele seturi.

        m - rows, n - cols
        T = O(m * n), S = O(m * n)
        """
        # rows, cols = len(heights), len(heights[0])
        # pac, atl = set(), set()

        # def dfs(r, c, visit, prevHeight):
        #     if ((r, c) in visit or
        #         r < 0 or c < 0 or
        #         r == rows or c == cols or
        #         heights[r][c] < prevHeight
        #     ):
        #         return
        #     visit.add((r, c))
        #     dfs(r + 1, c, visit, heights[r][c])
        #     dfs(r - 1, c, visit, heights[r][c])
        #     dfs(r, c + 1, visit, heights[r][c])
        #     dfs(r, c - 1, visit, heights[r][c])

        # for c in range(cols):
        #     dfs(0, c, pac, heights[0][c])
        #     dfs(rows - 1, c, atl, heights[rows - 1][c])

        # for r in range(rows):
        #     dfs(r, 0, pac, heights[r][0])
        #     dfs(r, cols - 1, atl, heights[r][cols - 1])

        # res = []
        # for r in range(rows):
        #     for c in range(cols):
        #         if (r, c) in pac and (r, c) in atl:
        #             res.append([r, c])
        # return res



        """BFS

        Aplică aceeași idee de „flux invers”, dar folosind BFS.

        O celulă poate curge către ocean dacă poți porni de la granița cu
        oceanul și te poți deplasa înapoi în grilă folosind regula:

        - din (r, c) poți ajunge la celula vecină (nr, nc) dacă
        heights[nr][nc] >= heights[r] [c] (deoarece, în direcția reală, apa ar
        curge de la o altitudine mai mare sau egală în jos către (r, c)).

        Deci:
        - Algoritmul BFS cu surse multiple, pornind de la toate celulele de
        la marginea Pacificului, marchează pac[r][c] = True
        - Algoritmul BFS cu surse multiple, pornind de la toate celulele de
        la marginea Atlanticului, marchează atl[r][c] = True

        Celulele care au valoarea True în ambele cazuri reprezintă răspunsul.

        m - rows, n - cols
        T = O(m * n), S = O(m * n)
        """
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac = [[False] * cols for _ in range(rows)]
        atl = [[False] * cols for _ in range(rows)]

        def bfs(source, ocean):
            q = collections.deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and
                        not ocean[nr][nc] and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        q.append((nr, nc))

        pacific = []
        atlantic = []
        for c in range(cols):
            pacific.append((0, c))
            atlantic.append((rows - 1, c))

        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols - 1))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res
