import collections


class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        """Brute Force (Backtracking)

        Pentru fiecare celulă goală (INF), încercăm să găsim cea mai scurtă
        cale către orice comoară (0) explorând toate cele 4 direcții folosind
        algoritmul DFS cu backtracking.

        - DFS explorează toate căile posibile pornind de la celulă până când
        întâlnește o comoară (distanța 0), un zid (-1) sau iese din zona de joc.
        - Folosim o grilă de vizite, astfel încât traseul curent să nu
        reviziteze celulele (ceea ce previne buclele infinite în cicluri).
        - Răspunsul pentru acea celulă este distanța minimă găsită dintre toate
        traseele DFS.

        Această metodă funcționează, dar este lentă, deoarece repetăm DFS din
        multe celule și reexplorăm aceleași zone de mai multe ori.

        T = O(m * n * 4^(m * n)), S = O(m * n)
        """
        # rows, cols = len(grid), len(grid[0])
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # INF = 2147483647
        # visit = [[False for _ in range(cols)] for _ in range(rows)]

        # def dfs(r, c):
        #     if (r < 0 or c < 0 or r >= rows or
        #         c >= cols or grid[r][c] == -1 or
        #         visit[r][c]):
        #         return INF
        #     if grid[r][c] == 0:
        #         return 0

        #     visit[r][c] = True
        #     res = INF
        #     for dx, dy in directions:
        #         res = min(res, 1 + dfs(r + dx, c + dy))
        #     visit[r][c] = False
        #     return res

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == INF:
        #             grid[r][c] = dfs(r, c)



        """BFS

        Algoritmul BFS este ideal pentru găsirea celui mai scurt drum într-o
        rețea neponderată. Pornind de la o celulă goală (INF), ne extindem
        nivel cu nivel (distanța 0, 1, 2, ...). Prima dată când ajungem la o
        celulă cu comoară (0), avem garanția că distanța reprezintă numărul
        minim de pași necesari.

        Această abordare execută un BFS separat pentru fiecare celulă INF,
        așa că este mai ușor de înțeles, dar poate fi totuși lentă, deoarece
        multe execuții BFS repetă aceeași operațiune.

        m - rows, n - cols
        T = O((m * n)^2), S = O(m * n)
        """
        # rows, cols = len(grid), len(grid[0])
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # INF = 2147483647

        # def bfs(r, c):
        #     q = collections.deque([(r, c)])
        #     visit = [[False] * cols for _ in range(rows)]
        #     visit[r][c] = True
        #     steps = 0
        #     while q:
        #         for _ in range(len(q)):
        #             row, col = q.popleft()
        #             if grid[row][col] == 0:
        #                 return steps
        #             for dr, dc in directions:
        #                 nr, nc = row + dr, col + dc
        #                 if (0 <= nr < rows and 0 <= nc < cols and
        #                     not visit[nr][nc] and grid[nr][nc] != -1
        #                 ):
        #                     visit[nr][nc] = True
        #                     q.append((nr, nc))
        #         steps += 1
        #     return INF

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == INF:
        #             grid[r][c] = bfs(r, c)



        """Multi Source BFS

        În loc să rulați BFS pornind din fiecare cameră goală, rulați BFS o
        singură dată, pornind simultan de la toate comorile (celulele cu
        valoarea 0).

        De ce funcționează acest lucru:
        - BFS se extinde în „valuri” cu distanțe de 0, 1, 2, ...
        - Dacă începem coada cu toate comorile, prima dată când valul ajunge
        la o celulă goală, acesta trebuie să provină de la cea mai apropiată
        comoară (deoarece BFS garantează că prima vizită este cea mai scurtă
        distanță într-o grilă neponderată).
        Astfel, fiecare celulă este completată cu distanța minimă față de
        orice comoară.

        Acest lucru evită repetarea operațiunilor și reprezintă abordarea
        optimă.

        m - rows, n - cols
        T = O(m * n), S = O(m * n)
        """
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = collections.deque()

        def add_cell(r, c):
            if (min(r, c) < 0 or r == rows or c == cols or
                (r, c) in visit or grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                add_cell(r + 1, c)
                add_cell(r - 1, c)
                add_cell(r, c + 1)
                add_cell(r, c - 1)
            dist += 1
