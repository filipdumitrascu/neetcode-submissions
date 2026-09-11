import collections

SIZE = 9
BOX = 3


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """Brute Force

        Verificam fiecare rand, coloana si patrat 3x3 cu un hash set pentru
        fiecare. Daca digitul curent se regaseste in structura de date, tabla
        e invalida. Aces approach parcurge intreaga tabla de 3 ori (o data
        pentru linii, o data pentru coloane si o data pentru patrate).

        n - SIZE
        T = O(n^2), S = O(n^2)
        """
        # for row in range(SIZE):
        #     seen = set()
        #     for j in range(SIZE):
        #         if board[row][j] == ".":
        #             continue
        #         if board[row][j] in seen:
        #             return False
        #         seen.add(board[row][j])

        # for column in range(SIZE):
        #     seen = set()
        #     for i in range(SIZE):
        #         if board[i][column] == ".":
        #             continue
        #         if board[i][column] in seen:
        #             return False
        #         seen.add(board[i][column])

        # for square in range(SIZE):
        #     seen = set()
        #     for i in range(BOX):
        #         for j in range(BOX):
        #             row = (square // BOX) * BOX + i
        #             column = (square % BOX) * BOX + j

        #             if board[row][column] == ".":
        #                 continue
        #             if board[row][column] in seen:
        #                 return False
        #             seen.add(board[row][column])

        # return True



        """Hash Set

        Diferenta fata de approachul anterior este ca in loc sa parcurgem de
        3 ori intreaga tabla verificand fiecare constraint (randuri fara duplicate,
        coloane, patrate fara duplicate), verificam daca celula curenta are
        valoarea deja in randul curent, coloana si patrat in acelasi timp.
        Astfel se face o singura parcurgere a tablei.

        T = O(n^2), S = O(n^2)
        """
        # cols = collections.defaultdict(set)
        # rows = collections.defaultdict(set)
        # squares = collections.defaultdict(set)

        # for r in range(SIZE):
        #     for c in range(SIZE):
        #         if board[r][c] == ".":
        #             continue
        #         if ( board[r][c] in rows[r] 
        #             or board[r][c] in cols[c]
        #             or board[r][c] in squares[(r // BOX, c // BOX)]
        #             ):
        #             return False

        #         cols[c].add(board[r][c])
        #         rows[r].add(board[r][c])
        #         squares[(r // BOX, c // BOX)].add(board[r][c])

        # return True



        """Bitmask

        Manipularea bitiilor poate reduce complexitatea spatiala.
        Fiecare cifra de la 1 la 9 poate fi reprezentata folosind un singur
        bit intr-un numar intreg. De exemplu, cifra 1 foloseste bitul 0,
        cifra 2 foloseste bitul 1, …, cifra 9 foloseste bitul 8.
        Aceasta inseamna ca putem urmari ce cifre au aparut intr-un rand, o
        coloana sau un patrat 3x3 folosind doar un singur numar intreg pentru
        fiecare rand, coloana sau caseta, in loc de un hash set.

        Cand întalnim o cifra, calculam pozitia bitului acesteia si verificam:
        daca acel bit este deja setat in rand, coloana sau patrat
        -> duplicat in rand, coloana sau patrat

        Daca niciuna dintre aceste verificari nu esueaza, 
        "activam” acel bit pentru a marca cifra ca fiind vazuta.

        T = O(n^2), S = O(n)
        """
        rows = [0] * SIZE
        cols = [0] * SIZE
        squares = [0] * SIZE

        for r in range(SIZE):
            for c in range(SIZE):
                if board[r][c] == ".":
                    continue

                # Each digit from 1 to 9 is mapped to a bit in the mask
                # (which has 9 bits, so 0–8); that's why 1 is subtracted.
                val = int(board[r][c]) - 1
                mask = 1 << val  # val's bit

                if mask & rows[r]:  # & checks if it is already in sudoku
                    return False

                if mask & cols[c]:
                    return False

                if mask & squares[(r // BOX) * BOX + (c // BOX)]:
                    return False

                rows[r] |= mask  # |= marks it as present in sudoku
                cols[c] |= mask
                squares[(r // BOX) * BOX + (c // BOX)] |= mask

        return True
