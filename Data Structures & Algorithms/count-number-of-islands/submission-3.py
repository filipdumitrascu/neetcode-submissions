import collections


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """DFS

        Se parcurge intreg gridul. Cand se gaseste o celula de
        pamant ("1"), se numara ca insula si cautam printr-o
        parcurgere DFS care celule alaturate sunt tot cu pamant.
        Astfel, le numaram si pe ele in cadrul aceleiasi insule.
        Se marcheaza fiecare celula cu pamant ca vizitata prin
        schimbarea valorii (din 1 in 0).

        m - nr de linii
        n - nr de coloane
        T = O(m * n), S = O(m * n)
        """
        # rows = len(grid)
        # cols = len(grid[0])
        # directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # def dfs(r: int, c: int) -> None:
        #     if (r < 0 or r >= rows or c < 0 or
        #         c >= cols or grid[r][c] == "0"
        #     ):
        #         return

        #     grid[r][c] = "0"

        #     for dr, dc in directions:
        #         dfs(r + dr, c + dc)

        # islands = 0
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1":
        #             dfs(r, c)
        #             islands += 1

        # return islands



        """BFS

        Acelasi lucru doar ca parcurgerea e BFS.

        T = O(m * n), S = O(m * n)
        """
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def bfs(r: int, c: int) -> None:
            q = collections.deque([(r, c)])
            grid[r][c] = "0"

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

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands
