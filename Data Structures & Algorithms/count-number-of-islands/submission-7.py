import collections


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """DFS

        T = O(rows * cols), S = O(rows * cols)
        """
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r: int, c: int) -> None:
            if (r < 0 or c < 0 or r >= rows or
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
