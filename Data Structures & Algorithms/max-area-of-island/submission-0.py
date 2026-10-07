import collections


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        """DFS

        Iteram prin grid si pentru fiecare "1" nevizitat,
        pornim un DFS care returneaza numarul de celule.

        m - rows, n - cols
        T = O(m * n), S = O(m * n)
        """
        # rows = len(grid)
        # cols = len(grid[0])
        # visit = set()

        # def dfs(r: int, c: int) -> int:
        #     if (r < 0 or r >= rows or c < 0 or
        #         c >= cols or grid[r][c] == 0 or
        #         (r, c) in visit
        #     ):
        #         return 0
        #     visit.add((r, c))

        #     return (1 + dfs(r + 1, c) +
        #                 dfs(r - 1, c) +
        #                 dfs(r, c + 1) + 
        #                 dfs(r, c - 1))

        # area = 0
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1:
        #             area = max(area, dfs(r, c))
        # return area



        """BFS

        Acelasi lucru doar ca parcurgerea e BFS.

        m - rows, n - cols
        T = O(m * n), S = O(m * n)
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        area = 0

        def bfs(r: int, c: int) -> int:
            q = collections.deque([(r, c)])
            grid[r][c] = 0
            res = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nr >= rows or nc < 0 or
                        nc >= cols or grid[nr][nc] == 0
                    ):
                        continue

                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    res += 1
            return res

        area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))
        return area
