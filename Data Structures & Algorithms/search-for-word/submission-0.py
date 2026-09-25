class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """Backtracking

        Trebuie să verificăm dacă cuvântul poate fi format parcurgând grila în
        sus/jos/stânga/dreapta, folosind fiecare celulă cel mult o singură
        dată pe același traseu.

        Așadar, pentru fiecare celulă, încercăm să începem cuvântul de acolo:
        -Dacă celula curentă corespunde caracterului curent, ne deplasăm către
        cele 4 celule învecinate pentru următorul caracter.
        -Pe parcursul explorării, marcăm celula ca vizitată (într-un set hash),
        astfel încât să nu o reutilizăm în același traseu.
        -Dacă un traseu eșuează, anulăm (ne întoarcem) vizita și încercăm
        alte direcții.

        Dacă reușim să potrivim toate caracterele, returnăm „true”
        (am găsit cuvântul).

        T = O(m * 4^n), S = O(n)
        """
        # rows, cols = len(board), len(board[0])
        # path = set()

        # def dfs(r, c, i):
        #     if i == len(word):
        #         return True

        #     if (min(r, c) < 0 or
        #         r >= rows or c >= cols or
        #         word[i] != board[r][c] or
        #         (r, c) in path):
        #         return False

        #     path.add((r, c))
        #     res = (dfs(r + 1, c, i + 1) or
        #            dfs(r - 1, c, i + 1) or
        #            dfs(r, c + 1, i + 1) or
        #            dfs(r, c - 1, i + 1))
        #     path.remove((r, c))
        #     return res

        # for r in range(rows):
        #     for c in range(cols):
        #         if dfs(r, c, 0):
        #             return True
        # return False



        """Backtracking Optimal

        Vrem să verificăm dacă cuvântul poate fi format prin deplasarea în
        sus/jos/stânga/dreapta în grilă, folosind fiecare celulă cel mult o
        singură dată într-un singur traseu.

        În loc să păstrăm o matrice separată a celulelor vizitate
        (spațiu suplimentar), marcăm temporar celula curentă ca fiind folosită,
        înlocuind caracterul acesteia cu o valoare specială (cum ar fi „#”).

        Aceasta înseamnă:
        Dacă vedem vreodată „#”, știm că această celulă se află deja în traseul
        nostru curent → nu o putem reutiliza.
        După ce explorăm pornind de la acea celulă, restabilim caracterul
        original (acesta este pasul de „retrogradare”), astfel încât alte
        trasee să o poată folosi.

        Așadar, ideea este următoarea:
        Încercați fiecare celulă ca punct de plecare.
        Efectuați o căutare în adâncime (DFS) pentru a potrivi cuvântul
        caracter cu caracter.
        Marcați → explorați vecinii → demarcați.

        T = O(m * 4^n), S = O(n)
        """
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False

            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
