import collections


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """BFS

        Aceasta este o problemă BFS cu surse multiple.

        Toate portocalele stricate (2) încep să răspândească putregaiul în
        același timp către portocalele proaspete învecinate (1).
        Fiecare nivel BFS reprezintă 1 minut.
        Dacă se ajunge la o portocală proaspătă, aceasta se strică în minutul
        următor.

        Idei cheie:
        - Porniți BFS pornind simultan de la toate portocalele stricate
        - Numărați câte portocale proaspete există
        - Fiecare nivel BFS = o unitate de timp
        - Dacă la final mai rămâne vreo portocală proaspătă → răspunsul este -1

        m - rows, n - cols
        T = O(m * n), S = O(m * n)
        """
        q = collections.deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
