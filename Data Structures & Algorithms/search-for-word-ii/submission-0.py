class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.idx = -1
        self.refs = 0

    def add_word(self, word, i):
        cur = self
        cur.refs += 1
        for c in word:
            index = ord(c) - ord('a')
            if not cur.children[index]:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
            cur.refs += 1
        cur.idx = i


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        """Brute Force    TLE

        Pentru fiecare cuvânt, încercăm să-l trasăm pe tablă parcurgând celulele
        adiacente (sus/jos/stânga/dreapta). Pentru a evita utilizarea aceleiași
        celule de două ori într-un traseu al cuvântului, marcăm temporar celula
        ca fiind vizitată, apoi o readucem la starea inițială după explorare
        (metoda clasică de backtracking).

        Dacă reușim să potrivim toate caracterele unui cuvânt în ordine, acel
        cuvânt este găsit și adăugat la rezultat.

        w - num(words) m - rows, n - cols, t - max(len(word))
        T = O(w * m * n * 4 * 3^t - 1), S = O(t)
        """        
        # rows, cols = len(board), len(board[0])
        # res = []

        # def backtrack(r, c, i):
        #     if i == len(word):
        #         return True

        #     if (r < 0 or c < 0 or r >= rows or
        #         c >= cols or board[r][c] != word[i]
        #     ):
        #         return False

        #     board[r][c] = '*'
        #     ret = (backtrack(r + 1, c, i + 1) or
        #            backtrack(r - 1, c, i + 1) or
        #            backtrack(r, c + 1, i + 1) or
        #            backtrack(r, c - 1, i + 1))
        #     board[r][c] = word[i]
        #     return ret

        # for word in words:
        #     flag = False
        #     for r in range(rows):
        #         if flag:
        #             break
        #         for c in range(cols):
        #             if board[r][c] != word[0]:
        #                 continue
        #             if backtrack(r, c, 0):
        #                 res.append(word)
        #                 flag = True
        #                 break
        # return res



        """Backtracking + Trie

În continuare efectuăm DFS pe graf, dar ghidăm DFS-ul folosind un arbore Trie, astfel încât să parcurgem doar căile care corespund prefixelor cuvintelor date.

Această versiune este mai rapidă deoarece introduce o tăiere agresivă:

Fiecare nod al arborelui Trie păstrează refs = „câte cuvinte din dicționar mai trec prin acest nod”.
Când găsim cu succes unul sau mai multe cuvinte, fiecare apel DFS returnează numărul de cuvinte noi pe care le-a găsit sub prefixul său curent.
Scădem acest număr din refs pe măsură ce DFS se derulează, eliminând cuvintele găsite din fiecare nod Trie de pe căile lor.
Dacă, după eliminare, valoarea refs a unui nod devine 0, acea ramură este moartă (niciun cuvânt rămas nu o mai folosește), așa că tăiem fizic pointerul de la părintele său (prev.children[...] = null).
Acest lucru împiedică apelurile DFS viitoare să exploreze prefixe inutile.
De asemenea, în loc să folosim un set de vizite, marcăm tabla pe loc:

Setăm temporar board[r][c] = «*» în timp ce explorăm acea cale.
Îl restabilim la revenire.
Ce stochează Trie-ul
Fiecare nod are:

children[26]: literele următoare (matrice, mai rapidă decât o hartă hash)
idx: indexul unui cuvânt în lista de cuvinte dacă un cuvânt se termină aici, altfel -1
refs: numărul de cuvinte „încă active” care trec prin acest nod (inclusiv cuvintele finale)


        T = O(), S = O()
        """
        root = TrieNode()
        for i in range(len(words)):
            root.add_word(words[i], i)

        rows, cols = len(board), len(board[0])
        res = []

        def get_index(c):
            index = ord(c) - ord('a')
            return index

        def dfs(r, c, node):
            if (r < 0 or c < 0 or r >= rows or
                c >= cols or board[r][c] == '*' or
                not node.children[get_index(board[r][c])]):
                return

            tmp = board[r][c]
            board[r][c] = '*'

            prev = node
            node = node.children[get_index(tmp)]

            if node.idx != -1:
                res.append(words[node.idx])
                node.idx = -1
                node.refs -= 1
                if not node.refs:
                    prev.children[get_index(tmp)] = None
                    node = None
                    board[r][c] = tmp
                    return

            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            board[r][c] = tmp

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res
