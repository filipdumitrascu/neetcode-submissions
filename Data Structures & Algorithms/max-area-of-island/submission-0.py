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

    def get_size(self, node):
        par = self.find(node)
        return self.size[par]


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        """DFS

        O insulă este un grup de celule „1” conectate între ele.
        Pentru a găsi aria maximă, explorăm fiecare insulă în întregime și
        numărăm câte celule conține.

        Căutarea în profunzime (dfs) ne ajută:
        - Începem de la o celulă de uscat
        - Vizităm toate celulele de uscat conectate (sus, jos, stânga, dreapta)
        - Numărăm dimensiunea acelei insule
        - Ținem evidența celei mai mari dimensiuni întâlnite

        Marcăm celulele ca fiind vizitate, astfel încât să nu numărăm aceeași
        celulă de două ori.

        m - rows, n - cols
        T = O(m * n), S = O(m * n)
        """
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or r == rows or c < 0 or
                c == cols or grid[r][c] == 0 or
                (r, c) in visit
            ):
                return 0

            visit.add((r, c))
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))

        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c))
        return area


        """BFS

        O insulă este un grup de celule marcate cu 1, conectate între ele.
        Pentru a găsi aria maximă, explorăm fiecare insulă în întregime și
        numărăm câte celule conține.

        Folosind metoda de căutare în lățime (BFS):
        - Începem de la o celulă de uscat (1)
        - Vizităm toate celulele de uscat conectate, nivel cu nivel
        - Considerăm fiecare celulă vizitată ca făcând parte din insulă
        - Marcăm celulele cu 0 pentru a evita revizitarea lor
        - Ținem evidența celei mai mari insule găsite

        m - rows, n - cols
        T = O(m * n), S = O(m * n)
        """
        # directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # rows, cols = len(grid), len(grid[0])
        # area = 0

        # def bfs(r, c):
        #     q = deque()
        #     grid[r][c] = 0
        #     q.append((r, c))
        #     res = 1

        #     while q:
        #         row, col = q.popleft()
        #         for dr, dc in directions:
        #             nr, nc = dr + row, dc + col
        #             if (nr < 0 or nc < 0 or nr >= rows or
        #                 nc >= cols or grid[nr][nc] == 0
        #             ):
        #                 continue
        #             q.append((nr, nc))
        #             grid[nr][nc] = 0
        #             res += 1
        #     return res

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1:
        #             area = max(area, bfs(r, c))

        # return area


        """DSU

        Gândește-te la fiecare celulă de uscat (1) ca la un nod dintr-un graf.
        Dacă două celule de uscat sunt adiacente (sus, jos, stânga, dreapta),
        ele aparțin aceleiași insule.

        Folosind metoda Disjoint Set Union (Union-Find):
        - Fiecare celulă de uscat începe ca o componentă separată
        - Când se găsesc două celule de uscat vecine, le unim
        - Dimensiunea unei componente conectate reprezintă suprafața acelei
        insule
        - Urmăriți dimensiunea maximă a componentei
        Această abordare este utilă atunci când doriți să grupați eficient
        componentele conectate.

        m - rows, n - cols
        T = O(m * n), S = O(m * n)
        """
        # rows, cols = len(grid), len(grid[0])
        # dsu = DSU(rows * cols)

        # def index(r, c):
        #     return r * cols + c

        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # area = 0

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1:
        #             for dr, dc in directions:
        #                 nr, nc = r + dr, c + dc
        #                 if (nr < 0 or nc < 0 or nr >= rows or
        #                     nc >= cols or grid[nr][nc] == 0
        #                 ):
        #                     continue

        #                 dsu.union(index(r, c), index(nr, nc))

        #             area = max(area, dsu.get_size(index(r, c)))

        # return area
