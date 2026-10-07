from collections import deque


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

        Iteram prin grid si de fiecare data cand gasim o
        celula de "1" nevizitata, pornim o parcurgere DFS
        pentru a le marca ca vizitate (le schimbam valoarea,
        din 1 in 0 de exemplu) pe toate celulele in vecinatatea
        acesteia. 

        m - rows, n - cols
        T = O(m * n), S = O(m * n)
        """
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # islands = 0

        # rows = len(grid)
        # cols = len(grid[0])

        # def dfs(r: int, c: int) -> None:
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

        Aceeasi idee doar ca parcurgerea e BFS.

        m - rows, n - cols
        T = O(m * n), S = O(m * n)        
        """
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # islands = 0

        # rows = len(grid)
        # cols = len(grid[0])

        # def bfs(r: int, c: int) -> None:
        #     q = deque([(r, c)])
        #     grid[r][c] = "0"

        #     while q:
        #         row, col = q.popleft()
        #         for dr, dc in directions:
        #             nr, nc = dr + row, dc + col

        #             if (nr < 0 or nc < 0 or nr >= rows or
        #                 nc >= cols or grid[nr][nc] == "0"
        #             ):
        #                 continue

        #             q.append((nr, nc))
        #             grid[nr][nc] = "0"

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1":
        #             bfs(r, c)
        #             islands += 1

        # return islands



        """DSU

        Tratam fiecare celula ca un nod unic intr-un graf.
        Parcurgem graful si pentru fiecare celula cu pamant,
        "1", o numaram ca insula. Daca celule pamant sunt
        adiacente, le conectam considerandu le parte din
        aceeasi insula / componenta conexa prin disjoint
        set union.

        m - rows, n - cols
        T = O(m * n), S = O(m * n) 
        """
        rows, cols = len(grid), len(grid[0])
        dsu = DSU(rows * cols)

        def graph_index(r, c):
            return r * cols + c

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '0':
                    continue

                islands += 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or nr >= rows or
                        nc >= cols or grid[nr][nc] == "0"
                    ):
                        continue

                    if dsu.union(graph_index(r, c), graph_index(nr, nc)):
                        islands -= 1

        return islands
