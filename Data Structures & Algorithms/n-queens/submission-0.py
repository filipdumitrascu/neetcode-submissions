class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        """Backtracking

        Scopul este de a plasa câte o regină în fiecare rând, astfel încât nici
        două regine să nu se atace reciproc.

        Observații cheie:
        - O regină poate ataca pe verticală, în diagonală spre stânga și în
        diagonală spre dreapta.
        - Deoarece plasăm reginele rând cu rând, de sus în jos, trebuie să
        verificăm doar rândurile situate deasupra rândului curent.
        - Dacă o poziție este sigură, plasăm o regină și trecem la rândul următor.
        - Dacă ajungem într-un impas, revenim asupra pașilor parcurși,
        eliminând ultima regină și încercând o altă coloană.

        Aceasta este o problemă clasică de backtracking combinată cu
        verificarea constrângerilor.

        T = O(n!), S = O(n^2)
        """
        # res = []
        # board = [["."] * n for i in range(n)]

        # def is_safe(r: int, c: int, board):
        #     row = r - 1
        #     while row >= 0:
        #         if board[row][c] == "Q":
        #             return False
        #         row -= 1

        #     row, col = r - 1, c - 1
        #     while row >= 0 and col >= 0:
        #         if board[row][col] == "Q":
        #             return False
        #         row -= 1
        #         col -= 1

        #     row, col = r - 1, c + 1
        #     while row >= 0 and col < len(board):
        #         if board[row][col] == "Q":
        #             return False
        #         row -= 1
        #         col += 1
        #     return True

        # def backtrack(r):
        #     if r == n:
        #         copy = ["".join(row) for row in board]
        #         res.append(copy)
        #         return
        #     for c in range(n):
        #         if is_safe(r, c, board):
        #             board[r][c] = "Q"
        #             backtrack(r + 1)
        #             board[r][c] = "."

        # backtrack(0)
        # return res



        """Backtracking (Hash Set)

        În loc să verificăm tabla de fiecare dată pentru a vedea dacă o regină
        este în siguranță, memorăm pozițiile atacate folosind seturi hash.

        Pentru orice regină aflată în poziția (rând, coloană):
        - Conflict de coloană → aceeași coloană
        - Conflict diagonal pozitiv → același (rând + coloană)
        - Conflict diagonal negativ → același (rând - coloană)
        Prin stocarea acestor informații în seturi, putem verifica dacă o 
        oziție este sigură în timp O(1).

        În continuare plasăm câte o regină pe rând, avansăm rând cu rând și 
        revenim înapoi atunci când o plasare duce la un conflict.

        T = O(n!), S = O(n^2)
        """
        # col = set()
        # pos_diag = set()
        # neg_diag = set()

        # res = []
        # board = [["."] * n for _ in range(n)]

        # # row by row
        # def backtrack(r):
        #     if r == n:
        #         copy = ["".join(row) for row in board]
        #         res.append(copy)
        #         return

        #     for c in range(n):
        #         # if this queen conflicts with an existing queen
        #         # on diagonal or column, it isn't added
        #         if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
        #             continue

        #         col.add(c)
        #         pos_diag.add(r + c)
        #         neg_diag.add(r - c)
        #         board[r][c] = "Q"

        #         backtrack(r + 1)

        #         col.remove(c)
        #         pos_diag.remove(r + c)
        #         neg_diag.remove(r - c)
        #         board[r][c] = "."

        # backtrack(0)
        # return res



        """Backtracking (Bit Mask)

        Aceasta este cea mai optimizată abordare de tip „backtracking” pentru
        problema celor N regine.

        În loc să folosim arrayuri sau seturi hash pentru a urmări coloanele
        și diagonalele ocupate, folosim măști de biți (numere întregi).
        Fiecare bit indică dacă o coloană sau o diagonală este deja ocupată.

        De ce funcționează bine:
        -Numerele întregi permit verificări de complexitate O(1) folosind 
        operații bit cu bit
        -Consumă foarte puțină memorie
        -În practică, este mai rapidă decât tabele/seturi

        Pentru o regină plasată în poziția (rând, coloană):
        -Masca coloanei → bitul coloanei
        -Diagonala pozitivă (/) → bitul (rând + coloană)
        -Diagonala negativă (\) → bitul (rând - coloană + n)
        -Dacă oricare dintre acești biți este deja setat, plasarea unei regine
        în acel loc provoacă un conflict.

        În continuare plasăm reginele rând cu rând, dar verificările de
        conflict se efectuează folosind operația AND bit cu bit.

        T = O(n!), S = O(n^2)
        """
        col = 0
        pos_diag = 0
        neg_diag = 0
        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            nonlocal col, pos_diag, neg_diag
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if ((col & (1 << c)) or (pos_diag & (1 << (r + c)))
                    or (neg_diag & (1 << (r - c + n)))):
                    continue
                col ^= (1 << c)
                pos_diag ^= (1 << (r + c))
                neg_diag ^= (1 << (r - c + n))
                board[r][c] = "Q"

                backtrack(r + 1)

                col ^= (1 << c)
                pos_diag ^= (1 << (r + c))
                neg_diag ^= (1 << (r - c + n))
                board[r][c] = "."

        backtrack(0)
        return res
