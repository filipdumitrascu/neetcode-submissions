import collections


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        """DFS

        O componentă conexă este un grup de noduri în care fiecare nod este
        accesibil din orice alt nod din acel grup.

        Folosind DFS:
        - Dacă începem DFS dintr-un nod nevizitat, vom vizita toate nodurile
        din componenta sa conexă.
        - De fiecare dată când începem DFS dintr-un nou nod nevizitat, am găsit
        o nouă componentă.

        v - vertices, e - edges
        T = O(v + e), S = O(v + e)
        """
        # adj = [[] for _ in range(n)]
        # visit = [False] * n
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)

        # def dfs(node):
        #     for nei in adj[node]:
        #         if not visit[nei]:
        #             visit[nei] = True
        #             dfs(nei)

        # res = 0
        # for node in range(n):
        #     if not visit[node]:
        #         visit[node] = True
        #         dfs(node)
        #         res += 1
        # return res



        """BFS

        O componentă conexă este un set de noduri în care fiecare nod poate
        ajunge la celelalte.

        Utilizarea algoritmului BFS:
        - Dacă pornim algoritmul BFS dintr-un nod nevizitat, acesta va vizita
        toate nodurile din acea componentă.
        - De fiecare dată când pornim algoritmul BFS dintr-un nou nod nevizitat,
        descoperim o nouă componentă conexă.

        v - vertices, e - edges
        T = O(v + e), S = O(v + e)
        """
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            q = collections.deque([node])
            visit[node] = True
            while q:
                cur = q.popleft()
                for nei in adj[cur]:
                    if not visit[nei]:
                        visit[nei] = True
                        q.append(nei)

        res = 0
        for node in range(n):
            if not visit[node]:
                bfs(node)
                res += 1
        return res



        """DSU (Rank | Size)

        Algoritmul Disjoint Set Union (DSU) grupează nodurile în componente
        conexe în mod eficient.

        - Începem prin a presupune că fiecare nod este propria sa componentă.
        - Când procesăm o muchie (u, v):
            - Dacă u și v se află deja în același set, nu se schimbă nimic.
            - Dacă se află în seturi diferite, le unim, iar numărul de
            componente scade cu 1.
        - Utilizarea uniunii după rang/dimensiune + compresia căilor asigură
        rapiditatea operațiunilor.

        La final, numărul de seturi rămase corespunde numărului de componente
        conectate.

        v - vertices, e - edges, alpha - amortized complexity
        T = O(v + e * alpha(v)), S = O(v + e)
        """
        # dsu = DSU(n)
        # res = n
        # for u, v in edges:
        #     if dsu.union(u, v):
        #         res -= 1
        # return res
