"""Abordari:

- DFS din orice celula pamant nevizitata (nemarcata in alta insula)

- BFS din orice celula pamant nevizitata (nemarcata in alta insula)

- Consider orice celula pamant ca fiind insula si fasc DSU
pentru a uni celulele vecine in aceeasi insula
"""


import collections


class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v) -> bool:
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

        T = O(rows * cols), S = O(rows * cols)
        """
        # rows = len(grid)
        # cols = len(grid[0])
        # directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # def dfs(r: int, c: int) -> None:
        #     if (r < 0 or c < 0 or r >= rows or
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

        T = O(rows * cols), S = O(rows * cols)
        """
        # rows = len(grid)
        # cols = len(grid[0])
        # directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # def bfs(r: int, c: int) -> None:
        #     q = collections.deque([(r, c)])
        #     grid[r][c] = "0"

        #     while q:
        #         row, col = q.popleft()
        #         for dr, dc in directions:
        #             new_row, new_col = row + dr, col + dc

        #             if (new_row < 0 or new_col < 0 or
        #                 new_row >= rows or new_col >= cols or
        #                 grid[new_row][new_col] == "0"
        #             ):
        #                 continue

        #             q.append((new_row, new_col))
        #             grid[new_row][new_col] = "0"

        # islands = 0
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1":
        #             bfs(r, c)
        #             islands += 1
        # return islands


        """DSU

        T = O(rows * cols), S = O(rows * cols)
        """
        rows = len(grid)
        cols = len(grid[0])
        dsu = DSU(rows * cols)

        def index(r: int, c: int) -> int:
            return r * cols + c

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (nr < 0 or nc < 0 or nr >= rows or
                            nc >= cols or grid[nr][nc] == "0"
                        ):
                            continue

                        if dsu.union(index(r, c), index(nr, nc)):
                            islands -= 1

        return islands