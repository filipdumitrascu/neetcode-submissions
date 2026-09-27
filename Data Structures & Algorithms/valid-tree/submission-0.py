import collections


class DSU:
    def __init__(self, n):
        self.comps = n
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

        self.comps -= 1
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.size[pu] += self.size[pv]
        self.parent[pv] = pu
        return True

    def components(self):
        return self.comps


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        """Cycle Detection (DFS)

        Un graf este un arbore valid dacă:
        - Nu conține cicluri
        - Este complet conectat

        Folosind DFS, putem detecta ciclurile verificând dacă vizităm din nou
        un nod pe o cale diferită de cea a părintelui său. De asemenea, un arbore
        cu n noduri trebuie să aibă exact n - 1 muchii — altfel nu este valid.

        v - vertices, e - edges
        T = O(v + e), S = O(v + e)
        """
        # if len(edges) > (n - 1):
        #     return False

        # adj = [[] for _ in range(n)]
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)

        # visit = set()
        # def dfs(node, par):
        #     if node in visit:
        #         return False

        #     visit.add(node)
        #     for nei in adj[node]:
        #         if nei == par:
        #             continue
        #         if not dfs(nei, node):
        #             return False
        #     return True

        # return dfs(0, -1) and len(visit) == n



        """BFS

        Un graf este un arbore valid dacă:
        - Nu conține cicluri
        - Este complet conex
        
        Folosind algoritmul BFS, parcurgem graful nivel cu nivel.
        - Dacă ajungem vreodată la un nod care a fost deja vizitat (și nu este
        părintele) → există un ciclu.
        - După aplicarea algoritmului BFS, dacă toate nodurile au fost vizitate,
        graful este conex.

        De asemenea, un arbore cu n noduri poate avea cel mult n - 1 muchii.

        v - vertices, e - edges
        T = O(v + e), S = O(v + e)
        """
        # if len(edges) > n - 1:
        #     return False

        # adj = [[] for _ in range(n)]
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)

        # visit = set()
        # q = collections.deque([(0, -1)])  # (current node, parent node)
        # visit.add(0)

        # while q:
        #     node, parent = q.popleft()
        #     for nei in adj[node]:
        #         if nei == parent:
        #             continue
        #         if nei in visit:
        #             return False
        #         visit.add(nei)
        #         q.append((nei, node))

        # return len(visit) == n



        """DSU

        Un graf este un arbore valid dacă:
        - Nu conține cicluri
        - Este complet conectat

        Folosind metoda „Disjoint Set Union” (Union-Find):
        - Fiecare nod începe în propria sa componentă
        - Când conectăm două noduri:
            - Dacă acestea se află deja în aceeași componentă, adăugarea acestei
            muchii creează un ciclu
            - În caz contrar, fuzionăm componentele lor
        - În final, un arbore valid trebuie să aibă exact o singură componentă
        conexă

        De asemenea, un arbore cu n noduri poate avea cel mult n - 1 muchii.

        v - vertices, e - edges
        T = O(v + e), S = O(v + e)
        """
        if len(edges) > n - 1:
            return False

        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        return dsu.components() == 1
