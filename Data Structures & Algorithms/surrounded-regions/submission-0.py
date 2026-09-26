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

    def connected(self, u, v):
        return self.find(u) == self.find(v)


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """DFS

        Doar regiunile „O” care ating marginea nu pot fi niciodată înconjurate,
        deoarece au o cale de ieșire în afara tablei de joc. Așadar, în loc să
        încercăm să găsim direct regiunile înconjurate, procedăm invers:

        - Marcăm toate celulele „O” conectate la margine ca fiind „sigure”
        (marcaj temporar „T”).
        - Orice „O” rămas este cu adevărat înconjurat → îl transformăm în „X”.
        - Transformăm marcajul temporar „T” înapoi în „O”.

        m - rows, n - cols
        T = O(m * n), S = O(m * n)
        """
        rows, cols = len(board), len(board[0])

        def capture(r, c):
            if (r < 0 or c < 0 or r == rows or
                c == cols or board[r][c] != "O"
            ):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for r in range(rows):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][cols - 1] == "O":
                capture(r, cols - 1)

        for c in range(cols):
            if board[0][c] == "O":
                capture(0, c)
            if board[rows - 1][c] == "O":
                capture(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"



        """BFS

        Aceeași idee ca în cazul DFS, dar folosim BFS cu o coadă.

        - Orice celulă „O” care este conectată la margine poate „evada”, așa că
        NU trebuie transformată.
        - Pornește BFS de la toate celulele „O” de la margine și marchează
        fiecare „O” accesibil cu un „T” temporar (în siguranță).
        - După aceea:
            - celulele „O” rămase sunt complet înconjurate → transformă-le în „X”
            - celulele „T” sunt în siguranță → transformă-le înapoi în „O”

        m - rows, n - cols
        T = O(m * n), S = O(m * n)
        """
        # rows, cols = len(board), len(board[0])
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # def capture():
        #     q = collections.deque()
        #     for r in range(rows):
        #         for c in range(cols):
        #             if (r == 0 or r == rows - 1 or
        #                 c == 0 or c == cols - 1) and board[r][c] == "O":
        #                 q.append((r, c))
        #     while q:
        #         r, c = q.popleft()
        #         if board[r][c] == "O":
        #             board[r][c] = "T"
        #             for dr, dc in directions:
        #                 nr, nc = r + dr, c + dc
        #                 if 0 <= nr < rows and 0 <= nc < cols:
        #                     q.append((nr, nc))

        # capture()
        # for r in range(rows):
        #     for c in range(cols):
        #         if board[r][c] == "O":
        #             board[r][c] = "X"
        #         elif board[r][c] == "T":
        #             board[r][c] = "O"



        """DSU

        Tratează fiecare celulă „O” ca pe un nod dintr-un graf. Două celule „O”
        aparțin aceleiași regiuni dacă sunt conectate în 4 direcții.

        Observația cheie:
        - Orice regiune de „O” care atinge marginea este sigură (nu poate fi
        înconjurată).
        - Orice regiune de „O” care nu atinge marginea este capturată → ar trebui
        să devină „X”.

        Așadar, folosim DSU (Union-Find) pentru a grupa celulele „O” conectate
        și creăm un nod fictiv suplimentar care reprezintă „conectat la margine”.
        - Unim fiecare „O” de la margine cu nodul fictiv.
        - Unim fiecare „O” cu celulele „O” învecinate.
        - În final, orice celulă care nu este conectată la nodul fictiv este
        înconjurată → se transformă în „X”.

        m - rows, n - cols
        T = O(m * n), S = O(m * n)
        """
        # rows, cols = len(board), len(board[0])
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # dsu = DSU(rows * cols + 1)

        # for r in range(rows):
        #     for c in range(cols):
        #         if board[r][c] != "O":
        #             continue
        #         if (r == 0 or c == 0 or
        #             r == (rows - 1) or c == (cols - 1)
        #         ):
        #             dsu.union(rows * cols, r * cols + c)
        #         else:
        #             for dx, dy in directions:
        #                 nr, nc = r + dx, c + dy
        #                 if board[nr][nc] == "O":
        #                     dsu.union(r * cols + c, nr * cols + nc)

        # for r in range(rows):
        #     for c in range(cols):
        #         if not dsu.connected(rows * cols, r * cols + c):
        #             board[r][c] = "X"
