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

        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(r: int, c: int) -> None:
            if (r < 0 or r >= rows or c < 0 or
                c >= cols or grid[r][c] == "0"
            ):
                return

            grid[r][c] = "0"

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands
