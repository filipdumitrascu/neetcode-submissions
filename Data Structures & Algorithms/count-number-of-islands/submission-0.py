import collections


class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        if self.size[pu] >= self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        return True


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """DFS

        Gândește-te la grilă ca la o hartă în care „1” reprezintă uscatul,
        iar „0” reprezintă apa. O insulă este un grup de celule de uscat
        conectate (sus, jos, stânga, dreapta). De fiecare dată când găsim o
        celulă de uscat care nu a fost vizitată, inițiem un DFS pentru a
        scufunda întreaga insulă, marcând tot uscatul conectat la aceasta ca
        apă. Fiecare apel DFS corespunde unei insule.

        m - rows, n - cols
        T = O(m * n), S = O(m * n)
        """
        # directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # rows, cols = len(grid), len(grid[0])
        # islands = 0

        # def dfs(r, c):
        #     if (r < 0 or c < 0 or r >= rows or
        #         c >= cols or grid[r][c] == "0"
        #     ):
        #         return

        #     grid[r][c] = "0"
        #     for dr, dc in directions:
        #         dfs(r + dr, c + dc)

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1":
        #             dfs(r, c)
        #             islands += 1

        # return islands



        """BFS

        Tratează grila ca pe o hartă în care „1” reprezintă uscatul, iar „0”
        reprezintă apa. Fiecare insulă este un grup de celule de uscat
        conectate între ele. Când întâlnim o celulă de uscat, folosim
        algoritmul BFS pentru a vizita toate celulele de uscat conectate și a
        le marca ca apă, asigurându-ne că aceeași insulă nu este 
        de două ori.

        m - rows, n - cols
        T = O(m * n), S = O(m * n)
        """
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= rows or
                        nc >= cols or grid[nr][nc] == "0"
                    ):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands



        """DSU

        Gândește-te inițial la fiecare celulă de uscat („1”) ca la o insulă
        separată. Când două celule de uscat sunt adiacente (sus, jos, stânga,
        dreapta), ele aparțin de fapt aceleiași insule, așa că ar trebui să
        le unim.

        Algoritmul „Disjoint Set Union” (Union-Find) ne ajută să:
        - Conectăm rapid celulele de uscat adiacente
        - Evităm să numărăm aceeași insulă de mai multe ori
        - Fiecare unire reușită reduce cu 1 numărul total de insule.

        m - rows, n - cols
        T = O(m * n), S = O(m * n)
        """
        # rows, cols = len(grid), len(grid[0])
        # dsu = DSU(rows * cols)

        # def index(r, c):
        #     return r * cols + c

        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # islands = 0

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == '1':
        #             islands += 1
        #             for dr, dc in directions:
        #                 nr, nc = r + dr, c + dc
        #                 if (nr < 0 or nc < 0 or nr >= rows or
        #                     nc >= cols or grid[nr][nc] == "0"
        #                 ):
        #                     continue

        #                 if dsu.union(index(r, c), index(nr, nc)):
        #                     islands -= 1

        # return islands
